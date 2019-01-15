from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://www.craftsvilla.com")
driver.implicitly_wait(10)
element=driver.find_element_by_xpath("//ul/li/a[text()='SAREES']")
# element=driver.find_element_by_xpath("//ul/li/a[text()='SALWAR SUITS ']")
act=ActionChains(driver)
time.sleep(2)
act.move_to_element(element).perform()