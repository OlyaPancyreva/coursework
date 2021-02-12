import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAuth(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get("http://localhost:8080/")

  def tearDown(self):
    time.sleep(5)
    self.driver.quit()

  def test_auth(self):
    self.driver.find_element(By.LINK_TEXT, "Вход").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bv-no-focus-ring > #login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bv-no-focus-ring > #login").send_keys("admin")
    self.driver.find_element(By.CSS_SELECTOR, ".bv-no-focus-ring > #password").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bv-no-focus-ring > #password").send_keys("admin")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


if __name__ == '__main__':
  unittest.main()
