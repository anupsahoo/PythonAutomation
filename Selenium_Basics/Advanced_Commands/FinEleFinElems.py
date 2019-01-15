from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.air.irctc.co.in/")
driver.implicitly_wait(20)
driver.find_element_by_xpath("//span[text()='Round Trip ']").click()
driver.find_element_by_id("from").send_keys("Bengaluru")
time.sleep(1)
driver.find_element_by_xpath("//div[contains(text(),'Bengaluru')]").click()
driver.find_element_by_id("to").send_keys("Boston")
time.sleep(1)
driver.find_element_by_xpath("//div[contains(text(),'Boston')]").click()
time.sleep(1)
driver.find_element_by_id("departureDate").click()
allmonths=driver.find_element_by_xpath("//div[@class='datepicker datepicker-dropdown datepicker-left datepicker-bottom rdeparturedate']").find_elements_by_xpath("//tr/td/span")
for i in range(len(allmonths)):
    if allmonths[i].size!=0:
        print(allmonths[i].text)
    driver.close()