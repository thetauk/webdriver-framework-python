import unittest
import logging
import sys
import requests
import subprocess
import time
from appium import webdriver

from tauk.tauk_webdriver import Tauk
from tauk.config import TaukConfig

from appium.webdriver.appium_service import AppiumService

from Resources.DataConfig import DataConfig

class BaseTest(unittest.TestCase):
  appium_service = AppiumService()
  logger = logging.getLogger()
  logger.level = logging.DEBUG
  stream_handler = logging.StreamHandler(sys.stdout)
  logger.addHandler(stream_handler)

  def setUp(self):
    if DataConfig.START_AND_STOP_APPIUM_STANDALONE:
      if self.appium_service.is_running == False:
        print("Appium starting: ")
        self.logger.info("Appium Starting...")
        pipe = self.appium_service.start(args=["--allow-cors", "--allow-insecure=get_server_logs"])
    else:
      self.logger.info("Appium should be running")
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