from selenium import webdriver
class Naukri():
    def allWIndows(self):
        driver=webdriver.Chrome()
        driver.get("http://www.naukri.com")
        wh=driver.window_handles
        print(len(wh))
ob=Naukri()
ob.allWIndows()