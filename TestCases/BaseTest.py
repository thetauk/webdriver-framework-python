import unittest
from appium import webdriver
from tauk.tauk_webdriver import Tauk

from Resources.DataConfig import DataConfig
from Resources.LogManager import LogManager
from Resources.AppiumManager import AppiumManager

class BaseTest(unittest.TestCase):
  logger = LogManager.setupLogging()

  def setUp(self):
    if DataConfig.START_AND_STOP_APPIUM_STANDALONE:
      check_pipe = AppiumManager.check_start_appium_service()
      if check_pipe:
        self.logger.info("Appium started using Appium Service")
    else:
      self.logger.info("Appium should be started already")
    self.logger.info(DataConfig.caps)
    self.driver = webdriver.Remote(command_executor = DataConfig.APPIUM_HOST, desired_capabilities = DataConfig.caps)
    Tauk.register_driver(self.driver, unittestcase=self)

  def tearDown(self):
    self.driver.quit()
    if DataConfig.START_AND_STOP_APPIUM_STANDALONE:
      if self.appium_service.is_running:
        print("Stopping appium.")
        self.logger.info("Appium Stopped.")
        self.logger.info(self.appium_service.stop())