from appium import webdriver

import unittest
from Pages.SpeedTestHomePage import SpeedTestHomePage
from Pages.ResultsPage import ResultsPage
from Resources.DataConfig import DataConfig
from TestCases.BaseTest import BaseTest
from tauk.tauk_webdriver import Tauk
from tauk.config import TaukConfig


class SpeedTest_ClickGo(BaseTest):
  def setUp(self):
    super().setUp()
    self.logger.info("Testing speedtest")
    self.driver = webdriver.Remote(command_executor=DataConfig.APPIUM_HOST, desired_capabilities=DataConfig.caps)


  def tearDown(self):
    self.driver.quit()
    super().tearDown()

  def test_click_go_button(self):
    speed_test_page = SpeedTestHomePage(self.driver)
    self.logger.info("Clicking Go Button")
    speed_test_page.click_go_button()
    results_page = ResultsPage(self.driver)
    results_page.wait_for_result()


if __name__ == '__main__':
  unittest.main()
