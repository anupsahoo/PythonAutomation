from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

class Verify_Login:

    def verify(self):
        Driver = webdriver.Chrome()
        base_url = "https://www.actimind.com/"
        Driver.get(base_url)
        Driver.maximize_window()

        action = ActionChains(Driver)
        element = Driver.find_element_by_xpath("//a[contains(text(), 'AREAS OF EXPERTISE')]")
        clk = Driver.find_element_by_xpath("//a[text()='Web Crawling']")
        action.move_to_element(element).click(clk).perform()
        time.sleep(100)
        print("Executed Successfully ")


login_test = Verify_Login()
login_test.verify()