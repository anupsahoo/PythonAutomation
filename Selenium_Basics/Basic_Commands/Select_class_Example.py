from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.select import Select
import time

class SelectClassExample():

    def select_class_example(self):
        baseUrl = "file:///C:/Users/5013505470/Desktop/pratice.html"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        drop_down_value = driver.find_element(By.ID, "carselect")
        select_obj = Select(drop_down_value)
        select_obj.select_by_index(1)
        select_obj.first_selected_option
        # select_obj.select_by_visible_text("Python")
        # select_obj.select_by_value("Selenium")
        time.sleep(5)
        print("All Select Class example executed")
        print_stack()

ff = SelectClassExample()
ff.select_class_example()