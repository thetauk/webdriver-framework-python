import functools
import unittest

from tauk.config import TaukConfig
from tauk.listeners.unittest_listener import TaukListener
from tauk.tauk_webdriver import Tauk
from optparse import OptionParser


from Resources.DataConfig import DataConfig
from Resources.AppiumManager import AppiumManager


class MyTestRunner(unittest.runner.TextTestRunner):

  def __init__(self, *args, **kwargs):
    """
    Append blacklist & whitelist attributes to TestRunner instance
    """

    super(MyTestRunner, self).__init__(*args, **kwargs)

  @classmethod
  def test_iter(cls, suite):
    """
    Iterate through test suites, and yield individual tests
    """
    for test in suite:
      if isinstance(test, unittest.TestSuite):
        for t in cls.test_iter(test):
          yield t
      else:
        yield test
  def run(self, testlist):
    suite = unittest.TestSuite()
    for test in self.test_iter(testlist):
      test_method = getattr(test, test._testMethodName)
      testlabels = getattr(test, "_labels", set())

      if DataConfig.include == '' and DataConfig.exclude == '' and DataConfig.test != '':
        suite.addTest(test)
      if DataConfig.include in testlabels:
        suite.addTest(test)
      if DataConfig.exclude in testlabels:
        @functools.wraps(test_method)
        def skip_wrapper(*args, **kwargs):
          raise unittest.SkipTest('label exclusion')

        skip_wrapper.__unittest_skip__ = True
        skip_wrapper.__unittest_skip_why__ = 'label exclusion'

        setattr(test, test._testMethodName, skip_wrapper)
        suite.addTest(test)
    super(MyTestRunner, self).run(suite)




if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option('-d', '--device', dest="udid", help='Enter device ID to run the test', default=True)
  parser.add_option('-t', '--test', dest="test", help='Enter test to run the test or all to run all', default="all")
  parser.add_option('-p', '--package', dest="package", help='App package', default=False)
  parser.add_option('-a', '--activity', dest="activity", help='App activity', default=False)
  parser.add_option('-b', '--bundleid', dest="bundleid", help='Bundle ID', default=False)
  parser.add_option('-o', '--os', dest="os", help='OS Type', default="Android")
  parser.add_option('-n', '--noreset', dest="noreset", help='No Reset capability', default=False)
  parser.add_option('-c', '--cloud', dest="cloud", help='Cloud URL', default=False)
  parser.add_option('-e', '--exclude', dest="exclude", help='Exclude Group', default=False)
  parser.add_option('-i', '--include', dest="include", help='Include Group', default=False)
  (option, arg) = parser.parse_args()

  #Setup desired capabilities from command line

  DataConfig.caps["appium:udid"] = option.udid
  DataConfig.caps["appium:deviceName"] = option.os
  DataConfig.caps["appium:platformName"] = option.os
  if option.noreset == "True" or option.noreset == "true":
    DataConfig.caps['appium:noReset'] = True

  if option.os == "Android":
    DataConfig.caps["appium:appPackage"] = option.package
    DataConfig.caps["appium:appActivity"] = option.activity
  else:
    DataConfig.caps["appium:bundleId"] = option.bundleid

  if option.exclude != False:
    DataConfig.exclude = option.exclude
  if option.include != False:
    DataConfig.include = option.include
  if hasattr(option, "cloud") and option.cloud != False:
    DataConfig.APPIUM_HOST = option.cloud
  else:
    DataConfig.APPIUM_HOST = "http://127.0.0.1:4723/wd/hub"

  if DataConfig.CHECK_START_APPIUM:
    AppiumManager.check_start_appium()

  Tauk(TaukConfig(api_token=DataConfig.TAUK_API_TOKEN, project_id=DataConfig.TAUK_PROJECT_ID))
  loader = unittest.TestLoader()
  if option.test == "all":
    DataConfig.test = option.test
    suite = loader.discover("./", pattern="test*.py")
  else:
    DataConfig.test = option.test
    suite = loader.discover("./", pattern=str(option.test) + ".py")
  alltests = unittest.TestSuite((suite))
  testRunner = MyTestRunner(resultclass=TaukListener, verbosity=2).run(alltests)
  #unittest.TextTestRunner(resultclass=TaukListener, verbosity=2).run(alltests)
  #punittest.main(testRunner=TextTestRunner(resultclass=TaukListener))