from selenium import webdriver
class Naukri():
    def noti(self):
        chrome_options=webdriver.ChromeOptions()
        prefs={"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        driver=webdriver.Chrome(chrome_options=chrome_options)
        driver.get("http://www.naukri.com")
        driver.save_screenshot("G:/Python/screenshot.png")

ob=Naukri()
ob.noti()