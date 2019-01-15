from FrameWork.base.Selenium_driver import SeleniumDriver

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        """

        :param driver:
        """
        super().__init__(driver)
        self.driver = driver

    _password="ap_password"
    _login="signInSubmit"

    def enterpassword(self):
        self.waitForElement(self._password, "id", 20, 0.5)
        self.sendKeys(self.readfromjson("pass"),self._password,"id")
        self.elementClick(self._login, "id")