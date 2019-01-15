from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToAlert():

    def test1(self):
        baseUrl = "file:///C:/Users/5013505470/Desktop/pratice.html"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element(By.ID, "name").send_keys("Pradeep")
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        print(alert1.text)
        alert1.accept()
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Rachit")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss()
        print("  Alert Executed Successfully  ")

ff = SwitchToAlert()
ff.test1()