from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class Verify_Login:

    def verify(self):
        Driver = webdriver.Chrome()
        base_url = "https://demo.actitime.com/login.do"
        Driver.get(base_url)
        Driver.implicitly_wait(10000)
        print("Used implict Wait")
        Driver.maximize_window()
        Driver.find_element_by_id("username").clear()
        Driver.find_element_by_id("username").send_keys('admin')
        Driver.find_element_by_name("pwd").clear()
        Driver.find_element_by_name("pwd").send_keys('manager')
        Driver.find_element_by_xpath("//a[@id='loginButton']").send_keys(Keys.ENTER)
        time.sleep(5)
        print("login is successful")


login_test = Verify_Login()
login_test.verify()