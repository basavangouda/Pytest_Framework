from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FinalPage:

    def __init__(self, driver):
        self.driver = driver

    def getValuesinField(self):
        return self.driver.find_element_by_xpath("//input[@id='country']").send_keys("ind")

    def getElementUntilClick(self):
        return self.driver.find_element_by_link_text("India").click()

    def getCheckBox(self):
        return self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

    def getPurchase(self):
        return self.driver.find_element_by_xpath("//input[@type='submit']").click()

    def getSuccessMessage(self):
        return self.driver.find_element_by_xpath("//strong[text()='Success!']").text