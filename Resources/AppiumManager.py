import requests
import subprocess
import time

from Resources.DataConfig import DataConfig

class AppiumManager:
  @staticmethod
  def check_start_appium():
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
        proc = subprocess.Popen(['appium', '--allow-insecure=get_server_logs', '--allow-cors'])
        print("Appium started" + str(proc.pid))
        i = 50
        while i > 0:
          try:
            requests.get('http://localhost:4723/wd/hub/status')
            break
          except:
            time.sleep(0.2)
            i = i - 1