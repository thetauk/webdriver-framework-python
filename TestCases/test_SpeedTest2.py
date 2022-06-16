
from Pages.SpeedTestHomePage import SpeedTestHomePage
from TestCases.BaseTest import BaseTest


class SpeedTest_VerifyGo(BaseTest):
  def setUp(self):
    super().setUp()
    self.logger.info("Testing speedtest")

  def tearDown(self):
    super().tearDown()

  def test_verify_go_button(self):
    print("*********Verify Go Button*******************************")
    print(self.driver)
    speed_test_page = SpeedTestHomePage(self.driver)
    self.logger.info("Verifying Go Button")
    speed_test_page.verify_go_button()

