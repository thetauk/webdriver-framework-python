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
  (option, arg) = parser.parse_args()
  DataConfig.caps["appium:udid"] = option.udid

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