from pages.checkbox_page import CheckBox
from selenium.webdriver.common.by import By


def test_single(browser):
    box_single = CheckBox(browser)
    box_single.open()
    box_single.check_click()
    box_single.button_click_submit()
    assert box_single.resul().text
