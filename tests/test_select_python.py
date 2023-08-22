from selenium.webdriver.common.by import By
from pages.select_python_page import SelectPythonPage


def test_select1_exist(browser):
    select_page = SelectPythonPage(browser)
    select_page.open()
    assert select_page.button_is_displayed()


def test_select2_click(browser):
    select_page = SelectPythonPage(browser)
    select_page.open()
    select_page.choose_lang().click()
    select_page.choose_click().click()
    select_page.button_click().click()
    assert select_page.result().text