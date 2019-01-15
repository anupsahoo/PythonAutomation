from selenium import webdriver
class AllLinks():
    def links(self):
        driver=webdriver.Chrome()
        driver.get("https://www.wikipedia.org/")
        driver.find_elements_by_tag_name("a")[2].click()

ob=AllLinks()
ob.links()
