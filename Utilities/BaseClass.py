import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_loggingDemo(self):
        loggerName= inspect.stack()[1][3] #This will give you the name from which method being called instaed of base class
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logging.log')
        formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger

    def VerifyText(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def SelectOption(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

