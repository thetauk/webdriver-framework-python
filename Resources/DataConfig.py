class DataConfig:

  ELEMENT_WAIT_TIME = 30
  LONG_WAIT_TIME = 120
  START_AND_STOP_APPIUM_STANDALONE = False
  CHECK_START_APPIUM = True
  LOCALHOST = "http://127.0.0.1"
  APPIUM_HOST = "http://127.0.0.1:4723/wd/hub"
  caps = {}
  caps['appium:deviceName'] = 'Android'
  caps['appium:platformName'] = 'Android'
  caps['appium:appPackage'] = 'org.zwanoo.android.speedtest'
  caps['appium:appActivity'] = 'com.ookla.mobile4.screens.main.MainActivity'
  caps['appium:noReset'] = True
  TAUK_PROJECT_ID = "veWbY3V9R"
  TAUK_API_TOKEN = "GkdEv-vulLl5iR628rJkRR5w"