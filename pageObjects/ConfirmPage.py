from selenium.webdriver.common.by import By

from pageObjects.FinalPage import FinalPage


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    def getCheckoutbutton(self):
         self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
         finalPage=FinalPage(self.driver)
         return finalPage