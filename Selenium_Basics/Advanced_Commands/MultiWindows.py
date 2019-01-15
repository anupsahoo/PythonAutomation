from selenium import webdriver
class Naukri():
    def allWIndows(self):
        driver=webdriver.Chrome()
        driver.get("http://www.naukri.com")
        wh=driver.window_handles
        for i in range(len(wh)):
            driver.switch_to.window(wh[i])
            print(driver.title)

ob=Naukri()
ob.allWIndows()