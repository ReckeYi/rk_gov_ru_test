from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import requests

url = "https://rk.gov.ru/profile/welcome"


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(7)
    return chrome_browser


def test_page_response(browser):
    response = requests.get(url)
    assert response.status_code == 200, f"Failed to get {url}. Status code: {response.status_code}"

    # title _sample5 claim__icon claim__icon_01


class TestAppealSection:
    def test_claim_esia(self, browser):
        browser.get(url)
        assert browser.find_element(By.CLASS_NAME, "claim__icon_01")

    def test_claim_esia_text_url(self, browser):
        browser.get(url)
        assert browser.find_element(By.CLASS_NAME, "claim__icon_01").click()



    def test_check_appeal_status_button_exist(self, browser):
        browser.get(url)
        assert browser.find_element(By.ID, "btn_edit")

    def test_check_appeal_status_button_clicked_empty_field(self, browser):
        browser.get(url)
        browser.find_element(By.ID, "btn_edit").click()
        assert browser.find_element(By.CLASS_NAME, "claim__error")
        assert "Неправильный код" == browser.find_element(By.CLASS_NAME, "claim__error").text
