import subprocess
import unittest
import time
from unittest import TextTestRunner

import requests
from tauk.config import TaukConfig
from tauk.listeners.unittest_listener import TaukListener
from tauk.tauk_webdriver import Tauk
from optparse import OptionParser


from Resources.DataConfig import DataConfig

if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option('-d', '--device', dest="udid", help='Enter device ID to run the test', default=True)
  parser.add_option('-t', '--test', dest="test", help='Enter test to run the test or all to run all', default=True)
  (option, arg) = parser.parse_args()
  DataConfig.caps["appium:udid"] = option.udid
  if DataConfig.CHECK_START_APPIUM:
    try:
      check_appium = requests.get('http://localhost:4723/wd/hub/status')
      if check_appium.status_code == 200:
        print("Appium already running")
      else:
        print("Appium may not be running. Status code: " + str(
          check_appium.status_code))
    except:
      print("Appium not running. Starting appium...")
      proc = subprocess.Popen(['appium', '--allow-insecure=get_server_logs'])
      print("Appium started" + str(proc.pid))
      i = 50
      while i > 0:
        try:
          requests.get('http://localhost:4723/wd/hub/status')
          break
        except:
          time.sleep(0.2)
          i = i - 1
  Tauk(TaukConfig(api_token=DataConfig.TAUK_API_TOKEN, project_id=DataConfig.TAUK_PROJECT_ID))
  loader = unittest.TestLoader()
  if option.test == "all":
    suite = loader.discover("./", pattern="test*.py")
  else:
    suite = loader.discover("./", pattern=str(option.test) + ".py")
  alltests = unittest.TestSuite((suite))
  unittest.TextTestRunner(resultclass=TaukListener, verbosity=2).run(alltests)
  #punittest.main(testRunner=TextTestRunner(resultclass=TaukListener))