import pytest
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def current_url(self):
        return self.driver.current_url

    def open_site_link(self, url):
        self.driver.get(url)