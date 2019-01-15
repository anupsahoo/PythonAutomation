from FrameWork.base.Selenium_driver import SeleniumDriver

class PD_Page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _availabity="//div[@id='centerCol']//div[@id='availability']/span"
    _addtocart="//div[@id='rightCol']//input[@id='add-to-cart-button']"


    def stockAvailabilty(self):
        """
        Checks for the stock availability
        :return: string
        """
        self.waitForElement(self._availabity, "xpath", 20, 0.5)
        status=self.getElement(self._availabity, "xpath").text
        status.replace(" ","")
        return status

    def addtocart(self):
        self.waitForElement(self._addtocart, "xpath", 20, 0.5)
        self.elementClick(self._addtocart,"xpath")

