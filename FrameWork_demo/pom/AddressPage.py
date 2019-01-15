from FrameWork.base.Selenium_driver import SeleniumDriver

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        """

        :param driver:
        """
        super().__init__(driver)
        self.driver = driver

    _deliveryaddress="//div[@id='address-book-entry-0']/div/span/a"
    _continue="//div[@class='a-box-inner']/span/span/input[@value='Continue']"

    def confirmaddress(self):
        self.waitForElement(self._deliveryaddress, "xpath", 20, 0.5)
        self.elementClick(self._deliveryaddress, "xpath")
        self.waitForElement(self._continue, "xpath", 20, 0.5)
        self.elementClick(self._continue, "xpath")



