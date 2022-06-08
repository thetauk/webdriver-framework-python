import unittest
import logging
import sys

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
    if self.appium_service.is_running == False:
      print("Appium starting: ")
      self.logger.info("Appium Starting...")
      print(self.appium_service.start(args=["--allow-cors", "--allow-insecure=get_server_logs"]))

  def tearDown(self):
    if self.appium_service.is_running:
      print("Stopping appium.")
      self.logger.info("Appium Stopped.")
      self.logger.info(self.appium_service.stop())