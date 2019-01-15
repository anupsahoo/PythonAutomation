from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToTab():

    def test1(self):
        baseUrl = "file:///C:/Users/5013505470/Desktop/pratice.html"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element(By.ID, "opentab").click()
        print(driver.current_window_handle)
        if (len(driver.window_handles) == 2):
            driver.switch_to.window(window_name=driver.window_handles[-1])
            # driver.close()
            driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div[1]/div[4]/span/a').click()
            # driver.switch_to.window(window_name=driver.window_handles[0])
            print(driver.current_window_handle)


ff = SwitchToTab()
ff.test1()