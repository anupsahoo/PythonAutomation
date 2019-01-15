from selenium import webdriver
class Naukri():
    def upload(self):
        driver=webdriver.Chrome()
        driver.get("https://www.monsterindia.com/")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//span[text()='Upload Resume']").click()
        driver.find_element_by_id("name").send_keys("Ramu")
        driver.find_element_by_id("mob_no").send_keys("9456127545")
        driver.find_element_by_id("wordresume").send_keys("G:/PythoSelenium/Resu.docx")
        driver.find_element_by_id("pop_sbm").click()
        Success=driver.find_element_by_xpath("//h1[@class='msg']").text
        print(Success)
ob=Naukri()
ob.upload()