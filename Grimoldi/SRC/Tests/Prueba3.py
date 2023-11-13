'''
Created on 27 oct. 2023

@author: joeln
'''
import time
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
from Functions.Functions import Functions as Selenium
from Functions.Inicializar import Inicializar as ini
import pytest_html
import msvcrt;
import unittest
import pytest



class Test03(unittest.TestCase):


    def setUp(self, URL=ini.URL):
        self.driver = webdriver.Chrome() #Abrir Chrome
        self.driver.implicitly_wait(10) #Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.maximize_window() #Maximizamos la ventana
        self.driver.get(URL)

    def test03(self):
        
        Selenium.get_json_file(self, 'Navj')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/compra/cart/')]")))
        
        Selenium.get_elements(self, 'Carrito').click()     
        
        msvcrt.getch()

    def testName(self):
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    pytest_html
    unittest.main()