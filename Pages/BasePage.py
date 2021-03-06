from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Resources.DataConfig import DataConfig

class BasePage:
  def __init__(self, driver):
    self.driver = driver

  def click_element(self, by_locator):
    WebDriverWait(self.driver, DataConfig.ELEMENT_WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).click()

  def wait_for_element(self, by_locator):
    WebDriverWait(self.driver, DataConfig.LONG_WAIT_TIME).until(EC.visibility_of_element_located(by_locator))

  def enter_text(self, by_locator, text):
    WebDriverWait(self.driver, DataConfig.ELEMENT_WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).send_keys(text)