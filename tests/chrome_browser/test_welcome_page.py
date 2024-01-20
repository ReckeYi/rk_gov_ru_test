from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

url = "https://rk.gov.ru/profile/welcome"
esia_url = "https://esia.gosuslugi.ru/login/"
create_url = "https://rk.gov.ru/profile/guest/petition/create"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'accept': '*/*'}


class TestPageStatus:
    def test_page_response(self, browser):
        response = requests.get(url=url, headers=headers)
        assert response.status_code == 200, f"Failed to get {url}. Status code: {response.status_code}"


class TestAppealSectionClaimWithEsiaProfile:
    def test_claim_with_esia_profile_exist(self, browser):
        browser.get(url)
        assert browser.find_element(By.CLASS_NAME, "claim__icon_01")

    def test_claim_with_esia_profile_text_url(self, browser):
        browser.get(url)
        browser.find_element(By.CLASS_NAME, "claim__icon_01").click()
        assert browser.current_url == esia_url


class TestAppealSectionClaimWithoutEsiaProfile:
    def test_claim_without_esia_profile_exist(self, browser):
        browser.get(url)
        assert browser.find_element(By.CLASS_NAME, "claim__icon_02")

    def test_claim_without_esia_profile_text_url(self, browser):
        browser.get(url)
        browser.find_element(By.CLASS_NAME, "claim__icon_02").click()
        assert browser.current_url == create_url


class TestAppealSectionCheckAppeal:

    def test_check_appeal_status_button_exist(self, browser):
        browser.get(url)
        assert browser.find_element(By.ID, "btn_edit")

    def test_check_appeal_status_button_clicked_with_empty_field(self, browser):
        browser.get(url)
        browser.find_element(By.ID, "btn_edit")
        browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        browser.find_element(By.ID, "btn_edit").click()
        assert browser.find_element(By.CLASS_NAME, "claim__error")
        assert "Неправильный код" == browser.find_element(By.CLASS_NAME, "claim__error").text

    def test_check_appeal_status_button_clicked_with_wrong_data_field_nums(self, browser):
        browser.get(url)
        code_input = browser.find_element(By.ID, "form_search")
        code_input.clear()
        code_input.send_keys("123456789")
        browser.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        browser.find_element(By.ID, "btn_edit").click()
        assert browser.find_element(By.CLASS_NAME, "claim__error")
        assert "Неправильный код" == browser.find_element(By.CLASS_NAME, "claim__error").text

    def test_check_appeal_status_button_clicked_with_wrong_data_field_rus_alph(self, browser):
        browser.get(url)
        code_input = browser.find_element(By.ID, "form_search")
        code_input.clear()
        code_input.send_keys("ФЫВФЫВФЫВ")
        browser.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        browser.find_element(By.ID, "btn_edit").click()
        assert browser.find_element(By.CLASS_NAME, "claim__error")
        assert "Неправильный код" == browser.find_element(By.CLASS_NAME, "claim__error").text

    def test_check_appeal_status_button_clicked_with_wrong_data_field_eng_alph(self, browser):
        browser.get(url)
        code_input = browser.find_element(By.ID, "form_search")
        code_input.clear()
        code_input.send_keys("ASDASDASDASD")
        browser.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        browser.find_element(By.ID, "btn_edit").click()
        assert browser.find_element(By.CLASS_NAME, "claim__error")
        assert "Неправильный код" == browser.find_element(By.CLASS_NAME, "claim__error").text
