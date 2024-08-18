import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome()
    browser.get(Urls.URL)
    yield browser
    browser.quit()

