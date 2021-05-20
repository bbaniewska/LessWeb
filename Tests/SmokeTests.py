import unittest
import time
from selenium import webdriver
from Config import Config
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProfilePage import ProfilePage
from Pages.SearchPage import SearchPage


class LessWeb(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get(Config.url)
        self.driver.maximize_window()

    def test_log_in_with_email(self):
        driver = self.driver
        homePage = HomePage(driver)
        homePage.slides_item_is_displayed()
        homePage.click_account_icon()
        homePage.account_icon_dropdown_is_displayed()
        homePage.click_login_label()
        loginPage = LoginPage(driver)
        loginPage.register_button_is_displayed()
        loginPage.facebook_button_is_displayed()
        loginPage.click_login_button()
        loginPage.send_login_email()
        loginPage.send_login_password()
        loginPage.click_submit_login_button()
        profilePage = ProfilePage(driver)
        profilePage.purchased_tab_is_displayed()

    def test_log_in_with_facebook(self):
        driver = self.driver
        homePage = HomePage(driver)
        homePage.slides_item_is_displayed()
        homePage.click_account_icon()
        homePage.account_icon_dropdown_is_displayed()
        homePage.click_login_label()
        loginPage = LoginPage(driver)
        loginPage.register_button_is_displayed()
        loginPage.click_facebook_button()
        loginPage.accept_facebook_cookie_policy()
        loginPage.send_login_email()
        loginPage.send_login_password()
        loginPage.click_facebook_button()
        profilePage = ProfilePage(driver)
        profilePage.purchased_tab_is_displayed()

    def test_like_product(self):
        driver = self.driver
        loginPage = LoginPage(driver)
        loginPage.log_in()
        searchPage = SearchPage(driver)
        searchPage.click_women_category()
        searchPage.fashion_women_title_is_displayed()
        searchPage.click_like_button()
        searchPage.assert_element_is_liked()

    def test_unlike_product(self):
        driver = self.driver
        loginPage = LoginPage(driver)
        loginPage.log_in()
        searchPage = SearchPage(driver)
        searchPage.click_women_category()
        searchPage.fashion_women_title_is_displayed()
        searchPage.click_like_button()
        searchPage.assert_element_is_liked()
        searchPage.click_like_button()
        searchPage.assert_element_is_unliked()

    #def test_edit_sale_post(self):

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()