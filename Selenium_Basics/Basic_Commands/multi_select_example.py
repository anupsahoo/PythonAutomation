from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.select import Select
import time

class MultiSelectClassExample():

    def multi_select_class_example(self):
        baseUrl = "file:///C:/Users/5013505470/Desktop/pratice.html"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        drop_down_value = driver.find_element(By.ID, "multiple-select-example")
        select_obj = Select(drop_down_value)
        select_obj.select_by_index(1)
        time.sleep(5)
        select_obj.select_by_index(2)
        time.sleep(3)
        # select_obj.select_by_value("Selenium")
        # select_obj.deselect_by_value("Selenium")
        # select_obj.select_by_visible_text("Automation")
        # select_obj.deselect_by_visible_text("Automation")
        print("All Select Class example executed")
        print_stack()

ff = MultiSelectClassExample()
ff.multi_select_class_example()