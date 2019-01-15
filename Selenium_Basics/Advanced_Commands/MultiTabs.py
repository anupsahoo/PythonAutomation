from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from datetime import timedelta
import time
presentmonth=datetime.datetime.now().strftime("%B")


cudate=datetime.datetime.now().strftime("%d")
dedate=datetime.datetime.now()+timedelta(days=20)
demonth=dedate.strftime("%B")
ardate=dedate+timedelta(days=50)
armonth=ardate.strftime("%B")
deptDate=dedate.strftime("%d")
arivDate=ardate.strftime("%d")

driver=webdriver.Chrome()
driver.implicitly_wait(20)

driver.maximize_window()
driver.get("https://www.irctc.co.in/nget/train-search")
parent=driver.current_window_handle
driver.find_element_by_xpath("//a[text()=' FLIGHTS ']").click()
twoTabs=driver.window_handles
for i in range(len(twoTabs)):
    if twoTabs[i]!=parent:
        driver.switch_to.window(twoTabs[i])
        print(driver.title)
        break
#WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH,"//span[text()='Round Trip ']"))
driver.find_element_by_xpath("//span[text()='Round Trip ']").click()
driver.find_element_by_id("from").send_keys("Bengaluru")
time.sleep(1)
driver.find_element_by_xpath("//div[contains(text(),'Bengaluru')]").click()
driver.find_element_by_id("to").send_keys("Boston")
time.sleep(1)
driver.find_element_by_xpath("//div[contains(text(),'Boston')]").click()
time.sleep(1)
driver.find_element_by_id("departureDate").click()
driver.find_element_by_xpath("//div[@class='datepicker datepicker-dropdown datepicker-left datepicker-bottom rdeparturedate']//tr/td/span[text()='"+str(demonth)+"']").click()
driver.find_element_by_xpath("//div[@class='datepicker datepicker-dropdown datepicker-left datepicker-bottom rdeparturedate']//span[contains(text(),'"+str(deptDate)+"')]").click()
driver.find_element_by_id("returnDate").click()
driver.find_element_by_xpath("//div[@class='datepicker datepicker-dropdown datepicker-left datepicker-bottom returnDate']//tr/td/span[text()='"+str(armonth)+"']").click()
driver.find_element_by_xpath("//div[@class='datepicker datepicker-dropdown datepicker-left datepicker-bottom returnDate']//span[contains(text(),'"+str(arivDate)+"')]").click()
driver.find_element_by_xpath("//button[text()='Search']").click()




