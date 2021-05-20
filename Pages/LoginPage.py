from selenium.webdriver.common.by import By
from Pages.CommonMethods import CommonMethods
from Pages.HomePage import HomePage


class LoginPage(CommonMethods):
    # SELECTORS_FOR_LOGIN_PAGE
    REGISTER_BUTTON = (By.XPATH, "//*[contains(@class, 'button-signup')]")
    FACEBOOK_BUTTON = (By.XPATH, "//*[contains(@class, 'button-facebook')]")
    LOGIN_BUTTON = (By.XPATH, "//*[contains(@class, 'button-login')]")
    LOGIN_EMAIL_INPUT = (By.ID, "loginEmail")
    LOGIN_PASSWORD_INPUT = (By.ID, "loginPassword")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class,'button-primary')]")
    FACEBOOK_COOKIE_ACCEPT_BUTTON = (By.ID, "u_0_8_FO")
    FACEBOOK_EMAIL_INPUT = (By.ID, "email")
    FACEBOOK_PASSWORD_INPUT = (By.ID, "pass")
    FACEBOOK_SUBMIT_LOGIN = (By.ID, "loginbutton")

    def register_button_is_displayed(self):
        self.assert_element_is_displayed(self.REGISTER_BUTTON)

    def facebook_button_is_displayed(self):
        self.assert_element_is_displayed(self.FACEBOOK_BUTTON)

    def click_login_button(self):
        self.wrapped_click(self.LOGIN_BUTTON)

    def send_login_email(self):
        self.wrapped_send_keys(self.LOGIN_EMAIL_INPUT, 'tester.less2020@gmail.com')

    def send_login_password(self):
        self.wrapped_send_keys(self.LOGIN_PASSWORD_INPUT, 'Test1234')

    def click_submit_login_button(self):
        self.wrapped_click(self.LOGIN_SUBMIT_BUTTON)

    def click_facebook_button(self):
        self.wrapped_click(self.FACEBOOK_BUTTON)

    def accept_facebook_cookie_policy(self):
        self.wrapped_click(self.FACEBOOK_COOKIE_ACCEPT_BUTTON)

    def send_facebook_login_email(self):
        self.wrapped_send_keys(self.FACEBOOK_EMAIL_INPUT, 'tester.less2020@gmail.com')

    def send_facebook_login_password(self):
        self.wrapped_send_keys(self.FACEBOOK_PASSWORD_INPUT, 'Test1234')

    def click_submit_facebook_login_button(self):
        self.wrapped_click(self.FACEBOOK_SUBMIT_LOGIN)

    def log_in(self):
        driver = self.driver
        homePage = HomePage(driver)
        homePage.click_account_icon()
        homePage.click_login_label()
        self.click_login_button()
        self.send_login_email()
        self.send_login_password()
        self.click_submit_login_button()