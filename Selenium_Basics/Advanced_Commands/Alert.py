from selenium import webdriver
import time
class AlertPopUp():
    def pop(self):
        driver=webdriver.Chrome()
        driver.execute_script("alert('QSpiders')")
        time.sleep(2)
        alrt=driver.switch_to_alert().text
        print(alrt)
        # driver.switch_to_alert().accept()
        driver.switch_to.alert.accept()
        time.sleep(2)


ob=AlertPopUp()
ob.pop()