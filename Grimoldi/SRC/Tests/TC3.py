'''

@author: vam99
'''
import unittest
import time
import msvcrt
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException

from selenium import webdriver

class TC_3(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome() #Abrir Chrome
        self.driver.implicitly_wait(10) #Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.maximize_window() 
  
        self.driver.get("https://www.grimoldi.com/")
        
   
    def testName(self):
        
        self.driver.find_element(By.XPATH, "//a[contains(@href, '/compra/cart/')]").click()
        time.sleep(2)
        link = self.driver.current_url
        print("URL actual:", link)
        
        
        msvcrt.getch()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()