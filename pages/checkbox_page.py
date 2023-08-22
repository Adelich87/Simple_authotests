from pages.base_page import BasePage
from selenium.webdriver.common.by import By

box_selector = (By.XPATH, '//input[@class="form-check-input"]')
submit_selector = (By.XPATH, '//input[@name="submit"]')
result_text = (By.ID, 'result-text')


class CheckBox(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')

    def check_click(self):
        return self.find(box_selector)

    def button_click_submit(self):
        return self.find(submit_selector)

    def result(self):
        return self.find(result_text)

    def resul(self):
        return self.find(result_text)