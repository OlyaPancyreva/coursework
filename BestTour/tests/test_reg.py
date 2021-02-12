import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestReg(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get("http://localhost:8080/")

  def tearDown(self):
    time.sleep(5)
    self.driver.quit()
  
  def test_reg(self):
    self.driver.find_element(By.LINK_TEXT, "Регистрация").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bv-no-focus-ring > #login-reg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bv-no-focus-ring > #login-reg").send_keys("Aleksey")
    self.driver.find_element(By.CSS_SELECTOR, ".bv-no-focus-ring > #email-reg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bv-no-focus-ring > #email-reg").send_keys("aleksey@mail.ru")
    self.driver.find_element(By.CSS_SELECTOR, ".bv-no-focus-ring > #password-reg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bv-no-focus-ring > #password-reg").send_keys("Geyan123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    assert self.driver.switch_to.alert.text == "Вы успешно зарегистрировались"
  

if __name__ == '__main__':
  unittest.main()