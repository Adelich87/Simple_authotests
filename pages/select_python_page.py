from pages.base_page import BasePage
from selenium.webdriver.common.by import By

submit_selector = (By.ID, 'submit-id-submit')
choose_selector = (By.ID, 'id_choose_language')
click_choose = (By.XPATH, '//option[@value="1"]')
result_text = (By.ID, 'result-text')


class SelectPythonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/select/single_select')

    def button_sel(self):
        return self.find(submit_selector)

    def button_is_displayed(self):
        return self.button_sel().is_displayed()

    def choose_lang(self):
        return self.find(choose_selector)

    def choose_click(self):
        return self.find(click_choose)

    def button_click(self):
        return self.find(submit_selector)

    def result(self):
        return self.find(result_text)