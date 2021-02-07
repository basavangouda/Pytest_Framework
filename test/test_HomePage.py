import pytest
from selenium import webdriver

from Utilities.BaseClass import BaseClass
from pageObjects.HomePageF import HomePageF
from selenium.webdriver.support.ui import Select

from pageObjects.TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):
    def test_Homepage(self,getData):
        log=self.get_loggingDemo()
        homepage=HomePageF(self.driver)
        log.info('Get the first name'+ getData["FirstName"])
        homepage.getName().send_keys(getData["FirstName"])
        homepage.getEmail().send_keys(getData["Email"])
        homepage.getPassword().send_keys("123345")
        homepage.getCheckbox()
        log.info("To know the Gender" + getData["Gender"])
        self.SelectOption(homepage.getGender(), getData["Gender"])
        homepage.getDoB()
        homepage.getSubmitButton()
        success= homepage.getSuccessMsg()


        assert success == "Success!"
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData('Test2'))
    def getData(self,request):
        return request.param



