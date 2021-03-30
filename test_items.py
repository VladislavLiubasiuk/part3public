import pytest
from selenium import webdriver

def test_if_button_is_present(browser):
    browser.implicitly_wait(5)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    looking = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert looking == "btn.btn-lg.btn-primary.btn-add-to-basket", "No button present!"
