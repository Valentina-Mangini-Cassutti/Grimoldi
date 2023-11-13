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



class TC_1107(unittest.TestCase, Selenium):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.grimoldi.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
    def safe_click(self, by, value):
        try:
            self.driver.find_element(by, value).click()
        except StaleElementReferenceException:
            # Retry the click in case of StaleElementReferenceException
            self.driver.find_element(by, value).click()

    def testName(self):
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "MUJER").click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.PARTIAL_LINK_TEXT, "MUJER")
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
            
        # Hacer clic en el enlace de la imagen "GRIMOLDI"
        try:
            self.driver.find_element(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img').click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img')
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)

        # HOMBRE
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "HOMBRE").click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.PARTIAL_LINK_TEXT, "HOMBRE")
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
            
           # Hacer clic en el enlace de la imagen "GRIMOLDI"
        try:
            self.driver.find_element(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img').click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img')
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)

        # NIÑOS
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "NIÑOS").click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.PARTIAL_LINK_TEXT, "NIÑOS")
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
               # Hacer clic en el enlace de la imagen "GRIMOLDI"
        try:
            self.driver.find_element(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img').click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img')
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)

        # ACCESORIOS
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "ACCESORIOS").click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except ElementClickInterceptedException:
            self.driver.execute_script("document.getElementById('wpnDialogId').style.display = 'none';")
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "ACCESORIOS").click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
            
               # Hacer clic en el enlace de la imagen "GRIMOLDI"
        try:
            self.driver.find_element(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img').click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img')
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)

# POR OCASIÓN
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "POR OCASIÓN").click()
            time.sleep(5)
            url_actual = self.driver.current_url  
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.PARTIAL_LINK_TEXT, "POR OCASIÓN")
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
            
               # Hacer clic en el enlace de la imagen "GRIMOLDI"
        try:
            self.driver.find_element(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img').click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img')
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)

        # MARCAS
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "MARCAS").click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.PARTIAL_LINK_TEXT, "MARCAS")
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
            
               # Hacer clic en el enlace de la imagen "GRIMOLDI"
        try:
            self.driver.find_element(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img').click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.XPATH, '//*[@id="sectorBanner_22972"]/a/img')
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)


        # OUTLET
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "OUTLET").click()
            time.sleep(5)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.safe_click(By.PARTIAL_LINK_TEXT, "OUTLET")
            time.sleep(3)
            url_actual = self.driver.current_url
            print("URL actual:", url_actual)
        
        # Hacer clic en el enlace "Volver a Grimoldi.com"
        wait = WebDriverWait(self.driver, 5)
        outlet_page_loaded = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='some-class-on-outlet-page']")))

        msvcrt.getch()

    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()
