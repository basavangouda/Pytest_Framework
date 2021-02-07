from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.FinalPage import FinalPage

class TestOne(BaseClass):
    def test_e2e(self):
        log=self.get_loggingDemo()
        homepage=HomePage(self.driver)
        CheckOutPage=homepage.shopItems()
        #self.driver.find_element_by_xpath("//a[text()='Shop']").click()


        #CheckOutPage = CheckoutPage(self.driver)
        #products = self.driver.find_elements_by_css_selector(".card-title a")
        log.info("Get all the product details")
        products=CheckOutPage.getProductName()


        for product in products:
            PN = product.text
            log.info(PN)
            if PN == 'Blackberry':
                '''self.driver.find_element_by_css_selector('.card-footer button').click()'''
                log.info(" Print the product information")
                CheckOutPage.getCardFooter().click()

        confirmPage=CheckOutPage.getCheckoutItem()
        #self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()


        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        finalPage= confirmPage.getCheckoutbutton()

        finalPage.getValuesinField()
        #self.driver.find_element_by_xpath("//input[@id='country']").send_keys("ind")

        '''wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'India')))

        self.driver.find_element_by_link_text("India").click()'''
        log.info("get the country details")
        self.VerifyText('India')

        finalPage.getElementUntilClick()

        #self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        finalPage.getCheckBox()


        #self.driver.find_element_by_xpath("//input[@type='submit']").click()
        finalPage.getPurchase()


        #msg = self.driver.find_element_by_xpath("//strong[text()='Success!']").text
        print(finalPage.getSuccessMessage())


