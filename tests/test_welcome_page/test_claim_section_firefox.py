from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

url = "https://rk.gov.ru/profile/welcome"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'accept': '*/*'}


class TestPageStatus:
    def test_page_response(self, ff_browser):
        """Response code Test"""
        response = requests.get(url=url, headers=headers)
        assert response.status_code == 200, f"Failed to get {url}. Status code: {response.status_code}"
        ff_browser.close()
        ff_browser.quit()

class TestAppealSectionClaimWithEsiaProfile:
    def test_claim_with_esia_profile_url_exist(self, ff_browser):
        """Claim with Esia profile url exist: url exists test."""
        ff_browser.get(url)
        assert ff_browser.find_element(By.CLASS_NAME, "claim__icon_01")
        ff_browser.close()
        ff_browser.quit()

    def test_claim_with_esia_profile_text_url(self, ff_browser):
        """Claim with Esia profile text url: text url redirect test."""
        ff_browser.get(url)
        ff_browser.find_element(By.CLASS_NAME, "claim__icon_01").click()
        assert ff_browser.current_url == "https://esia.gosuslugi.ru/login/"
        ff_browser.close()
        ff_browser.quit()


class TestAppealSectionClaimWithoutEsiaProfile:
    def test_claim_without_esia_profile_url_exist(self, ff_browser):
        """Claim without Esia profile url login exist: url exists test."""
        ff_browser.get(url)
        assert ff_browser.find_element(By.CLASS_NAME, "claim__icon_02")
        ff_browser.close()
        ff_browser.quit()

    def test_claim_without_esia_profile_text_url(self, ff_browser):
        """Claim without Esia profile login text url: text url redirect test."""
        ff_browser.get(url)
        ff_browser.find_element(By.CLASS_NAME, "claim__icon_02").click()
        assert ff_browser.current_url == "https://rk.gov.ru/profile/guest/petition/create"
        ff_browser.close()
        ff_browser.quit()


class TestAppealSectionFAQ:
    def test_faq_url_exist(self, ff_browser):
        """FAQ url exist: url exists test."""
        ff_browser.get(url)
        assert ff_browser.find_element(By.CLASS_NAME, "claim__icon_03")
        ff_browser.close()
        ff_browser.quit()

    def test_claim_without_esia_profile_text_url(self, ff_browser):
        """FAQ url: url redirect test."""
        ff_browser.get(url)
        ff_browser.find_element(By.CLASS_NAME, "claim__icon_03")
        ff_browser.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        ff_browser.find_element(By.CLASS_NAME, "claim__icon_03").click()
        assert ff_browser.current_url == "https://rk.gov.ru/profile/guest/petition/faq"
        ff_browser.close()
        ff_browser.quit()


class TestAppealSectionCheckAppeal:

    def test_check_appeal_status_button_exist(self, ff_browser):
        """Check Appeal Status Button Exist: button exists test."""
        ff_browser.get(url)
        assert ff_browser.find_element(By.ID, "btn_edit")
        ff_browser.close()
        ff_browser.quit()

    def test_check_appeal_status_button_clicked_with_empty_field(self, ff_browser):
        """Check appeal status button clicked with empty field: submit failed test."""
        ff_browser.get(url)
        ff_browser.find_element(By.ID, "btn_edit")
        ff_browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        ff_browser.find_element(By.ID, "btn_edit").click()
        assert ff_browser.find_element(By.CLASS_NAME, "claim__error")
        assert "Неправильный код" == ff_browser.find_element(By.CLASS_NAME, "claim__error").text
        ff_browser.close()
        ff_browser.quit()

    def test_check_appeal_status_button_clicked_with_wrong_data_field_nums(self, ff_browser):
        """Check appeal status button clicked with wrong data field nums: submit failed test."""
        ff_browser.get(url)
        code_input = ff_browser.find_element(By.ID, "form_search")
        code_input.clear()
        code_input.send_keys("123456789")
        ff_browser.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        ff_browser.find_element(By.ID, "btn_edit").click()
        assert ff_browser.find_element(By.CLASS_NAME, "claim__error")
        assert "Неправильный код" == ff_browser.find_element(By.CLASS_NAME, "claim__error").text
        ff_browser.close()
        ff_browser.quit()

    def test_check_appeal_status_button_clicked_with_wrong_data_field_rus_alph(self, ff_browser):
        """Check appeal status button clicked with wrong data russian alphabet: submit failed test."""
        ff_browser.get(url)
        code_input = ff_browser.find_element(By.ID, "form_search")
        code_input.clear()
        code_input.send_keys("ФЫВФЫВФЫВ")
        ff_browser.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        ff_browser.find_element(By.ID, "btn_edit").click()
        assert ff_browser.find_element(By.CLASS_NAME, "claim__error")
        assert "Неправильный код" == ff_browser.find_element(By.CLASS_NAME, "claim__error").text
        ff_browser.close()
        ff_browser.quit()

    def test_check_appeal_status_button_clicked_with_wrong_data_field_eng_alph(self, ff_browser):
        """Check appeal status button clicked with wrong data english alphabet: submit failed test."""
        ff_browser.get(url)
        code_input = ff_browser.find_element(By.ID, "form_search")
        code_input.clear()
        code_input.send_keys("ASDASDASDASD")
        ff_browser.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        ff_browser.find_element(By.ID, "btn_edit").click()
        assert ff_browser.find_element(By.CLASS_NAME, "claim__error")
        assert "Неправильный код" == ff_browser.find_element(By.CLASS_NAME, "claim__error").text
        ff_browser.close()
        ff_browser.quit()
