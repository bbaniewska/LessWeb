from selenium.webdriver.common.by import By
import time
from .CommonMethods import CommonMethods


class HomePage(CommonMethods):
    # SELECTORS_FOR_HOME_PAGE
    SLIDES_ITEM = (By.XPATH, "//*[@class='slides-item'][1]")
    ACCOUNT_ICON = (By.XPATH, "//*[@class='icon-account']")
    ACCOUNT_ICON_DROPDOWN = (By.XPATH, "//*[contains(@class, 'active')]//*[@class='dropdown']")
    ACCOUNT_ICON_LOGIN_LABEL = (By.LINK_TEXT, "Login")

    def slides_item_is_displayed(self):
        self.assert_element_is_displayed(self.SLIDES_ITEM)

    def click_account_icon(self):
        self.wrapped_click(self.ACCOUNT_ICON)

    def account_icon_dropdown_is_displayed(self):
        self.assert_element_is_displayed(self.ACCOUNT_ICON_DROPDOWN)

    def click_login_label(self):
        self.wrapped_click(self.ACCOUNT_ICON_LOGIN_LABEL)
