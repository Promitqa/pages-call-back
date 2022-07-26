import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # browser = webdriver.Chrome(chrome_options=options)
    browser = webdriver.Chrome()
    browser.implicitly_wait(7)
    yield browser
    print("\nquit browser..")
    browser.quit()
