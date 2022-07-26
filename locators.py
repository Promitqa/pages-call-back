from selenium.webdriver.common.by import By


class MainPageLocators:
    FIND_BUTTON = (By.CLASS_NAME, "recall_popup_button")
    INPUT_LINK = (By.CLASS_NAME, "cpopup__input")
    FIND_POPUP = (By.CLASS_NAME, "cpopup__win")
