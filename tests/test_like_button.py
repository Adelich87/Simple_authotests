from selenium.webdriver.common.by import By
from pages.like_button_page import LikeAButton


def test_button2_exist(browser):
    like_a_button = LikeAButton(browser)
    like_a_button.open()
    assert like_a_button.button_is_displayed


def test_button2_clicked(browser):
    like_a_button = LikeAButton(browser)
    like_a_button.open()
    like_a_button.button.click()
    assert 'Submitted' == like_a_button.result_text
