import time

def test_if_button_is_present(browser):
    browser.implicitly_wait(5)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #time.sleep(30)
    browser.get(link)
    looking = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert looking, "No button present!"
