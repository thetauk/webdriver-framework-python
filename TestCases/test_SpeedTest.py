import unittest
from unittest import TextTestRunner

from tauk.listeners.unittest_listener import TaukListener

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

  def tearDown(self):
    super().tearDown()

  def test_click_go_button(self):
    print("*************************************************")
    print(self.driver)
    speed_test_page = SpeedTestHomePage(self.driver)
    self.logger.info("Clicking Go Button")
    speed_test_page.click_go_button()
    results_page = ResultsPage(self.driver)
    results_page.wait_for_result()


# if __name__ == '__main__':
#   Tauk(TaukConfig(api_token=DataConfig.TAUK_API_TOKEN,
#                   project_id=DataConfig.TAUK_PROJECT_ID))
#   unittest.main(testRunner=TextTestRunner(resultclass=TaukListener))
