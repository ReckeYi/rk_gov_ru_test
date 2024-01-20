from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(6)
    return chrome_browser


@pytest.fixture()
def ff_browser():
    firefox_browser = webdriver.Firefox()
    firefox_browser.implicitly_wait(6)
    return firefox_browser


