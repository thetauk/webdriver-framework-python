from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class ByjusHomePage(BasePage):
  GET_STARTED = (By.ID, "com.byjus.thelearningapp:id/layoutLoginPhoneNumber")
  ENTER_NUMBER = (By.ID, "com.byjus.thelearningapp:id/etPhoneNumber")
  NONE_OF_THE_ABOVE = (By.ID, "com.google.android.gms:id/cancel")
  PHONE_NUMBER = "9999999999"
  def click_get_started(self):
    return self.click_element(self.GET_STARTED)

  def click_none_of_the_above(self):
    return self.click_element(self.NONE_OF_THE_ABOVE)

  def enter_phone_number(self):
    return self.enter_text(self.ENTER_NUMBER, self.PHONE_NUMBER)