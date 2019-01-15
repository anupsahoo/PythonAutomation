from selenium import webdriver
import time
class Naukri():
    def allWIndows(self):
        driver=webdriver.Chrome()
        driver.get("http://www.naukri.com")
        wh=driver.window_handles
        for i in range(len(wh)):
            driver.switch_to.window(wh[i])
            if i%2==1:
                driver.close()
        time.sleep(5)
ob=Naukri()
ob.allWIndows()