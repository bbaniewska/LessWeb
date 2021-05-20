from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonMethods:
    TIMEOUT = 30

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)

    def wait_for_element(self, locator, time=TIMEOUT):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def assert_element_is_displayed(self, element):
        self.find_element(element).is_displayed()
        return self

    def wrapped_click(self, element):
        self.find_element(element).click()

    def wrapped_send_keys(self, locator, element):
        self.find_element(locator).send_keys(element)

    def assert_element_is_liked(self, element):
        colour = self.find_element(element).getCssValue('stroke')
        return colour == 'rgb(200, 5, 70)'

    def assert_element_is_unliked(self, element):
        colour = self.find_element(element).getCssValue('stroke')
        return colour == 'rgb(0, 0, 0)'
