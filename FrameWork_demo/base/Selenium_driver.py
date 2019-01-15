from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from FrameWork.utilties.custom_logger import customLogger
from selenium.webdriver.support.ui import Select
# from FrameWork.utilties.ExcelReader import readExcel
import os.path
import logging

class SeleniumDriver():

    log = customLogger(logging.DEBUG)
    # excel = readExcel.getCSVData()


    def __init__(self, driver):
        """
                Inits WebDriver class

                Returns:
                    None
                """
        self.driver = driver

    def getByType(self, locatorType):
        """
        It takes Locator type and
        Returns: locator
        """
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getMethodName(self, name):
        global methodname
        methodname = name

    def getElement(self, locator, locatorType="id"):
        """

        :param locator: path of element in html
        :param locatorType: locator to find the element
        :return: web element
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def getElements(self, locator, locatorType="id"):
        """

        :param locator: path of element in html
        :param locatorType: locator to find the element
        :return: list of web element
        """
        elements = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return elements

    def getTitle(self):
        return self.driver.title

    def mousehovering(self,locator,locatorType="id"):
        """
        It does mouse hovering to a particular element
        :param locator: path of element in html
        :param locatorType: locator to find the element
        :return: None
        """
        act=ActionChains(self.driver)
        act.move_to_element(self.getElement(locator, locatorType)).perform()

    def elementClick(self, locator, locatorType="id"):
        """

        :param locator: path of element in html
        :param locatorType: locator to find the element
        :return: None
        """
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        """

        :param data: data to enter in text box
        :param locator: path of element in html
        :param locatorType: locator to find the element
        :return: None
        """
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        """

        :param locator: path of element in html
        :param locatorType: locator to find the element
        :return: boolean
        """
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        """

                :param locator: path of element in html
                :param locatorType: locator to find the element
                :return: boolean
                """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        """

                :param locator: path of element in html
                :param locatorType: locator to find the element
                :param timeout: time to wait
                :param pollFrequency: poll time period to search for the element
                :return: element
                """
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element


    def selectItem(self,vtext,locator,locatorpath="id"):
        """
        To select option from drop down
        :param vtext: visible text
        :param locator: element path
        :param locatorpath: element locator
        :return: None
        """
        sel = Select(self.getElement(locator, locatorpath))
        sel.select_by_visible_text(vtext)

    def get_screenshot(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        _screenshotpath = os.path.join(my_path, "../ScreenShots/" + methodname + ".png")
        self.driver.save_screenshot(_screenshotpath)
