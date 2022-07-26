from locators import MainPageLocators
from base_page import BasePage


class MainPage(BasePage):
    def find_element_button(self):
        button = self.browser.find_element(*MainPageLocators.FIND_BUTTON)
        button.click()

        assert self.browser.find_element(*MainPageLocators.FIND_POPUP)

        input1 = self.browser.find_element(*MainPageLocators.INPUT_LINK)
        input1.send_keys("111 111 11 11")

        assert self.browser.find_element(*MainPageLocators.INPUT_LINK)
