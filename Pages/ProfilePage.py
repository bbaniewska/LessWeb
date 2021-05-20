from selenium.webdriver.common.by import By
import time
from Pages.CommonMethods import CommonMethods


class ProfilePage(CommonMethods):
    # SELECTORS_FOR_PROFILE_PAGE
    FOLLOW_COUNTERS_TITLE = (By.XPATH, "//span[contains(text(), 'Followers')]")
    PURCHASED_TAB = (By.XPATH, "//a[contains(text(),'Purchased')]")

    def follow_counters_item_is_displayed(self):
        self.assert_element_is_displayed(self.FOLLOW_COUNTERS_TITLE)

    def purchased_tab_is_displayed(self):
        self.assert_element_is_displayed(self.PURCHASED_TAB)
