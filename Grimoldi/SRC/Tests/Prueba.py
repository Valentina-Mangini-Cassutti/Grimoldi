import unittest
import time
import msvcrt
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
from Functions.Functions import Functions as Selenium



import unittest
from selenium import webdriver
import time

class TC_1107(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.grimoldi.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
    def testName(self):
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self, "Mujer").click()
        time.sleep(2) 
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self, "Grimoldi").click()
        time.sleep(2)   
        
        


if __name__ == "__main__":
    unittest.main()



            
        
    