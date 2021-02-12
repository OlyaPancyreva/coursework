import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/")

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_request(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn-req").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-req")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("Игорь")
        self.driver.find_element(By.ID, "mail").click()
        self.driver.find_element(By.ID, "mail").send_keys("igor_2@gmail.com")
        self.driver.find_element(By.ID, "phone").click()
        self.driver.find_element(By.ID, "phone").send_keys("89420154221")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


if __name__ == '__main__':
    unittest.main()
