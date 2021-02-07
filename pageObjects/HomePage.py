from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver=driver

    shope = (By.XPATH,"//a[text()='Shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shope).click()
        CheckOutPage = CheckoutPage(self.driver)
        return CheckOutPage

