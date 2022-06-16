import unittest

from tauk.config import TaukConfig
from tauk.listeners.unittest_listener import TaukListener
from tauk.tauk_webdriver import Tauk
from optparse import OptionParser


from Resources.DataConfig import DataConfig
from Resources.AppiumManager import AppiumManager

if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option('-d', '--device', dest="udid", help='Enter device ID to run the test', default=True)
  parser.add_option('-t', '--test', dest="test", help='Enter test to run the test or all to run all', default=True)
  parser.add_option('-p', '--package', dest="package", help='App package', default=False)
  parser.add_option('-a', '--activity', dest="activity", help='App activity', default=False)
  parser.add_option('-b', '--bundleid', dest="bundleid", help='Bundle ID', default=False)
  parser.add_option('-o', '--os', dest="os", help='OS Type', default=True)
  parser.add_option('-n', '--noreset', dest="noreset", help='OS Type', default=False)
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

  # caps['appium:appPackage'] = 'org.zwanoo.android.speedtest'
  # caps['appium:appActivity'] = 'com.ookla.mobile4.screens.main.MainActivity'
  if DataConfig.CHECK_START_APPIUM:
    AppiumManager.check_start_appium()

  Tauk(TaukConfig(api_token=DataConfig.TAUK_API_TOKEN, project_id=DataConfig.TAUK_PROJECT_ID))
  loader = unittest.TestLoader()
  if option.test == "all":
    suite = loader.discover("./", pattern="test*.py")
  else:
    suite = loader.discover("./", pattern=str(option.test) + ".py")
  alltests = unittest.TestSuite((suite))
  unittest.TextTestRunner(resultclass=TaukListener, verbosity=2).run(alltests)
  #punittest.main(testRunner=TextTestRunner(resultclass=TaukListener))