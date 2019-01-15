from selenium import webdriver

class SwitchToTab():

    def test1(self):
        baseUrl = "https://timesofindia.indiatimes.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(2) > a').click()
        driver.execute_script("window.scrollBy(0, 3000);")
        driver.switch_to.frame(driver.find_element_by_css_selector('#pollframe'))
        driver.find_element_by_css_selector('#pollform > div > a:nth-child(1)').click()
        print("iframe script executed successfully")



ff = SwitchToTab()
ff.test1()