from selenium.webdriver.support.ui import Select
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/Rohsmiles/Desktop/sample.html")
element=driver.find_element_by_id("Fruits")
sel=Select(element)
sel.select_by_visible_text("Apple")
sel.select_by_visible_text("Pomegranate")
Elemen=sel.options
for i in range(len(Elemen)):
    print(Elemen[i].text)