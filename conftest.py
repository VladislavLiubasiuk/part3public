import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
#Есть одна важная особенность поведения конфигурационных файлов, о которой вы обязательно должны знать.
#PyTest автоматически находит и подгружает файлы conftest.py, которые находятся в директории с тестами. 
#Если вы храните все свои скрипты для курса в одной директории, будьте аккуратны и следите, чтобы не возникало ситуации, 
#когда вы запускаете тесты из папки tests:
#tests/
#├── conftest.py
#├── subfolder
#│   └── conftest.py
#│   └── test_abs.py
#следует избегать!
#В таком случае применяется ОБА файла conftest.py, что может вести к непредсказуемым ошибкам и конфликтам.
#selenium_course_solutions/
#├── section3
#│   └── conftest.py
#│   └── test_languages.py
#├── section4 
#│   └── conftest.py
#│   └── test_main_page.py
#правильно!

