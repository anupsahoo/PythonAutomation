from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptExecution():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get("file:///C:/Users/5013505470/Desktop/pratice.html")
        driver.execute_script("window.location = 'C:/Users/5013505470/Desktop/pratice.html';")
        driver.implicitly_wait(3)
        time.sleep(6)

        # element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")

ff = JavaScriptExecution()
ff.test()