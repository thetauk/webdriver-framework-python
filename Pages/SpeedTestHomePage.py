from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
###SpeedTest is used as the sample here

class SpeedTestHomePage(BasePage):
  GO_BUTTON = (By.ID, "org.zwanoo.android.speedtest:id/go_button")
  def __init__(self, driver):
    super().__init__(driver)

  def click_go_button(self):
    return self.click_element(self.GO_BUTTON)

