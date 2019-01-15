from FrameWork.base.Selenium_driver import SeleniumDriver

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        """

        :param driver:
        """
        super().__init__(driver)
        self.driver = driver

    _proceedtocheckout="hlb-ptc-btn-native"

    def gotosignup(self):
        self.waitForElement(self._proceedtocheckout, "id", 20, 0.5)
        self.elementClick(self._proceedtocheckout, "id")