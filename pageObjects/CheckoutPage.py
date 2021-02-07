from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def getProductName(self):
        return self.driver.find_elements_by_css_selector(".card-title a")

    def getCardFooter(self):
        return self.driver.find_element_by_css_selector('.card-footer button')

    def getCheckoutItem(self):
        self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
        confirmPage=ConfirmPage(self.driver)
        return confirmPage



