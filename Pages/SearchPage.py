from selenium.webdriver.common.by import By
import time
from .CommonMethods import CommonMethods


class SearchPage(CommonMethods):
    # SELECTORS_FOR_SEARCH_PAGE
    FASHION_WOMEN_CATEGORY = (By.XPATH, "//span[contains(text(), 'Women')]")
    FASHION_WOMAN_TITLE = (By.XPATH, "//h2[contains(text(), 'Fashion')]")
    LIKE_BUTTON = (By.XPATH, "//*[@class='post'][1]//div[@class='preview']//button[@id='like-button']")
    MARKED_LIKE_BUTTON = (
    By.XPATH, "//*[@class='post'][1]//div[@class='preview']//button[@id='like-button']//*[@stroke='rgb(0,0,0)']")

    def click_women_category(self):
        self.wrapped_click(self.FASHION_WOMEN_CATEGORY)

    def fashion_women_title_is_displayed(self):
        self.assert_element_is_displayed(self.FASHION_WOMAN_TITLE)

    def click_like_button(self):
        self.wrapped_click(self.LIKE_BUTTON)

    def check_like_button_is_marked(self):
        self.assert_element_is_liked(self.MARKED_LIKE_BUTTON)
