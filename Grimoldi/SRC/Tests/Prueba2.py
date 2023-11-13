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


from selenium import webdriver

class Prueba2(unittest.TestCase):


    def setUp(self):
        self.json_strings = False
        self.driver = webdriver.Chrome() #Abrir Chrome
        self.driver.implicitly_wait(10) #Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.maximize_window() 
  
        self.driver.get("https://www.grimoldi.com/")
    
   
   
    def testName(self):
        
        """
        while True:
            try:
                # Busca el botón "AHORA NO" en la página
                element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "AHORA NO")
        
                # Una vez que se encuentra el elemento, haz clic en él
                element.click()
                print("Se hizo clic en el botón 'AHORA NO'.")
                break  # Rompe el bucle si se hizo clic en el botón
            except Exception as e:
                # Maneja la excepción si el botón no se encuentra en el ciclo actual
                print("El botón 'AHORA NO' no se encontró en la página en este ciclo.")
                self.driver.refresh()
                """
            
    #MUJER
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "MUJER")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"calzadomujer").click()
        time.sleep(2)
        
        #-----
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "MUJER")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"aircollection").click()
        time.sleep(2)
        
        #-----
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "MUJER")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"accesoriosmujer").click()
        time.sleep(2)
        
        #-----
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "MUJER")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"apie").click()
        time.sleep(2)
        
     #HOMBRE
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "HOMBRE")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"calzadohombre").click()
        time.sleep(2)
        
        #-----
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "HOMBRE")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"airhombre").click()
        time.sleep(2)
        
        #-----
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "HOMBRE")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"accesorioshombre").click()
        time.sleep(2)
        
        #-----
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "HOMBRE")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"hushpuppies").click()
        time.sleep(2)
        
        
    #NIÑOS
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "NIÑOS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"calzadoninos").click()
        time.sleep(2)
        
        #-----
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "NIÑOS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"accesoriosninos").click()
        time.sleep(2)
        
        #-----
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "NIÑOS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"Kickers").click()
        time.sleep(2)
        
    #ACCESORIOS 

        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "ACCESORIOS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"accesorios_mujer").click()
        time.sleep(2)
        
        #-----
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "ACCESORIOS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"accesorios_hombre").click()
        time.sleep(2)
        
        #POR OCASIÓN
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "POR OCASIÓN")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"zapatosnoche").click()
        time.sleep(2)
        
        #---
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "POR OCASIÓN")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"loselegidosdecorine").click()
        time.sleep(2)
        
    #MARCAS
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, "MARCAS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 3)
        
        Selenium.get_json_file(self, "Navj")
        Selenium.get_elements(self,"vans").click()
        time.sleep(2)


    
        
        msvcrt.getch()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()