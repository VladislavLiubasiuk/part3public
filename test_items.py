import pytest
from selenium import webdriver

def test_if_button_is_present(browser):
    browser.implicitly_wait(5)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    looking = browser.find_element_by_class_name("no-js")
    user_language = looking.get_attribute("lang")
    if user_language == "es":
        result1 = browser.find_element_by_class_name("btn.btn-lg.btn-primary").text
        assert result1 == "Añadir al carrito", "WRONG TEXT!"
    elif user_language == "fr":
        result1 = browser.find_element_by_class_name("btn.btn-lg.btn-primary").text
        assert result1 == "Ajouter au panier", "WRONG TEXT!"
