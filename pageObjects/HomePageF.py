from selenium.webdriver.common.by import By

class HomePageF:

    def __init__(self, driver):
        self.driver= driver

    def getName(self):
        return self.driver.find_element_by_name("name")

    def getEmail(self):
        return self.driver.find_element_by_name('email')

    def getPassword(self):
        return self.driver.find_element_by_id("exampleInputPassword1")

    def getCheckbox(self):
        return self.driver.find_element_by_id("exampleCheck1").click()

    def getGender(self):
        return self.driver.find_element_by_id("exampleFormControlSelect1")

    def getDoB(self):
        return self.driver.find_element_by_name("bday").send_keys("08-06-1994")

    def getSubmitButton(self):
        return self.driver.find_element_by_xpath("//input[@class='btn btn-success']").click()

    def getSuccessMsg(self):
        return self.driver.find_element_by_css_selector('.alert-success strong').text