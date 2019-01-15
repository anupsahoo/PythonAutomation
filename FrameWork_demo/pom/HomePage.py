from FrameWork.base.Selenium_driver import SeleniumDriver
from FrameWork.utilties.AllFileReaders import allFilesReaders
from selenium.webdriver.common.action_chains import ActionChains
import xlrd

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        """

        :param driver:
        """
        super().__init__(driver)
        self.driver = driver
        self.af_reader=allFilesReaders()

    #locators
    _shop_by_category="nav-link-shopall"
    _search_box="twotabsearchtextbox"
    _search_button="//div/input[@class='nav-input' and @value='Go']"
    _subcategory="//div[@id='navbar']//div[@id='nav-flyout-shopAll']/div/span/span"
    _sign_in = "//div[@id='nav-tools']/a/span[text()='Your Orders']"
    _signin_button="//div[@id='nav-flyout-ya-signin']/a/span[text()='Sign in']"
    _email="ap_email"
    _continue="continue"
    _password="ap_password"
    _login="signInSubmit"
    _signout="//div[@id='nav-flyout-yourAccount']//a/span[text()='Sign Out']"

    def searchproduct(self, key):
        """

        :param product: product to be searched
        :return: boolean
        """
        self.sendKeys(self.af_reader.readfromjson(key),self._search_box,"id")
        self.elementClick(self._search_button,"xpath")
        return True

    def shopbycategorymenus(self):
        """
        Fetching categories under shop by category
        :return: list of categories
        """
        self.mousehovering(self._shop_by_category,"id")
        self.waitForElement(self._subcategory, "xpath", 10, 0.5)
        menus=self.getElements(self._subcategory,"xpath")
        menutext = [x.text for x in menus]
        return menutext

    def login(self, user, pwd):
        self.mousehovering(self._sign_in,"xpath")
        self.elementClick(self._signin_button,"xpath")
        self.sendKeys(self.af_reader.readfromjson(user), self._email, "id")
        self.elementClick(self._continue, "id")
        self.sendKeys(self.af_reader.readfromjson(pwd), self._password, "id")
        self.elementClick(self._login, "id")


    def logout(self):
        self.waitForElement(self._sign_in, "xpath", 20, 0.5)
        self.mousehovering(self._sign_in,"xpath")
        self.elementClick(self._signout, "xpath")










