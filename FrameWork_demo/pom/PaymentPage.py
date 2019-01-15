from FrameWork.base.Selenium_driver import SeleniumDriver

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        """

        :param driver:
        """
        super().__init__(driver)
        self.driver = driver

    _creditcard="//div[@class='a-box pmts-instrument-box']//input[@value='SelectableAddCreditCard']"
    _cardnumber="//div/label[text()='Card number']/following-sibling::input[@name='addCreditCardNumber']"
    _date="//span[@class='a-button-inner']/span[@data-action='a-dropdown-button']/span[text()='01']"

    def payment(self):
        self.self.waitForElement(self._creditcard, "xpath", 20, 0.5)
        self.elementClick(self._creditcard, "xpath")
        self.sendKeys(self.readfromjson("card"), self._cardnumber, "xpath")
        self.elementClick(self._date, "xpath")



