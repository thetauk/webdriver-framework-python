from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class ResultsPage(BasePage):
  TEST_AGAIN_BUTTON = (By.ID, "org.zwanoo.android.speedtest:id/suite_completed_feedback_assembly_test_again")
  def __init__(self, driver):
    super().__init__(driver)
  def wait_for_result(self):
    self.wait_for_element(self.TEST_AGAIN_BUTTON)


