from FrameWork.pom.HomePage import HomePage
from FrameWork.base.Selenium_driver import SeleniumDriver
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp","getStatus")
class Test_search(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.home_page = HomePage(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.usefixtures("login")
    def test_loginAmazon(self):
        self.sd.getMethodName(self.__class__.__name__)
        assert "Online Shopping site in India" in self.sel_driver.getTitle()

