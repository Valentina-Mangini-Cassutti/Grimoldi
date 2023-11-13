''''

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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


from selenium import webdriver

class TC_2(unittest.TestCase):


    def setUp(self):
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

        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/calzadomujer/']")))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))
       
           
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"MUJER")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/aircollection/']")))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))   
        
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"MUJER")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/accesoriosmujer/']" )))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))
            
            
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"MUJER")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located(((By.XPATH, "//a[@href='/a-pie/']"))))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))
            
         
        #Hombre
           
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"HOMBRE")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located(((By.XPATH, "//a[@href='/calzadohombre/']"))))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))          
            
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"HOMBRE")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located(((By.XPATH, "//a[@href='/airhombre/']"))))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e)) 
             
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"HOMBRE")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/accesorioshombre/']" )))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))
            
            
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"HOMBRE")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try: 

            element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/cat/']" )))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))
        
        #Niños
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"NIÑOS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located(((By.XPATH, "//a[@href='/calzadoninos/']"))))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))          
            
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"NIÑOS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located(((By.XPATH, "//a[@href='//accesoriosninos//']"))))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e)) 
             
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"NIÑOS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try: 

            element = wait.until(EC.presence_of_element_located(((By.XPATH, "//a[@href='/Kickers/']"))))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))        
        
    #ACCESORIOS
    
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"ACCESORIOS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located(((By.XPATH, "//a[@href='/accesoriosmujer/']"))))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))          
            
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"ACCESORIOS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located(((By.XPATH, "//a[@href='/accesorioshombre/']"))))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e)) 
             
        
            
    #POR OCACIÓN
    
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"POR OCASIÓN")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located(((By.XPATH, "//a[@href='/zapatosnoche/']"))))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))          
            
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"POR OCASIÓN")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        try:
            element = wait.until(EC.presence_of_element_located(((By.XPATH, "//a[@href='/loselegidosdecorine/']"))))
            element.click()
            time.sleep(2)
            link = self.driver.current_url
            print("URL actual:", link)
        except Exception as e:
            print("Error:", str(e))   
        
            
    #MARCAS        
        
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT,"MARCAS")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)         
                    
        wait = WebDriverWait(self.driver, 3) 

        
        element = wait.until(EC.presence_of_element_located((By.XPATH, "/a[@href='/vans/']")))
        element.click()
        time.sleep(2)
        link = self.driver.current_url
        print("URL actual:", link)

        
       
        
        
        msvcrt.getch()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()