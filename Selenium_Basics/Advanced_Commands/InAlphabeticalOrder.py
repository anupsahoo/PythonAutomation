from selenium.webdriver.support.ui import Select
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/Rohsmiles/Desktop/sample.html")
element=driver.find_element_by_id("Fruits")
sel=Select(element)
Elemen=sel.options
alpElement=[]
for i in range(1,len(Elemen)):
    alpElement.append(Elemen[i].text)
print(sorted(alpElement))