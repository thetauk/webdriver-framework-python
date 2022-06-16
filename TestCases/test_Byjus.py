from TestCases.BaseTest import BaseTest
from Pages.ByjusHomePage import ByjusHomePage

class ByjusApp(BaseTest):
  def setUp(self):
    super().setUp()
    self.logger.info("Testing speedtest")

  def tearDown(self):
    super().tearDown()

  def test_click_get_started(self):
    byjus_home_page = ByjusHomePage(self.driver)
    # try:
    #   byjus_home_page.click_get_started()
    # except:
    #   self.logger.info("No get started button")
    try:
      byjus_home_page.click_none_of_the_above()
    except:
      self.logger.info("No number prompting screen")

    byjus_home_page.enter_phone_number()