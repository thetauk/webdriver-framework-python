from Pages.SpeedTestHomePage import SpeedTestHomePage
from Pages.ResultsPage import ResultsPage
from TestCases.BaseTest import BaseTest


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
