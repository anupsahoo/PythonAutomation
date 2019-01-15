from selenium.webdriver.support.ui import Select
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/Rohsmiles/Desktop/sample.html")
element=driver.find_element_by_id("Fruits")
sel=Select(element)
wbE=element.find_element_by_xpath("//option[@value='1']").text
sel.select_by_index(1)
print(wbE)