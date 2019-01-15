from FrameWork.pom.HomePage import HomePage
from FrameWork.pom.PL_Page import PL_Page
from FrameWork.base.Selenium_driver import SeleniumDriver
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp","getStatus")
class Test_search(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.home_page = HomePage(self.driver)
        self.pl_page = PL_Page(self.driver)
        self.sd=SeleniumDriver(self.driver)

    @pytest.mark.run(order=1)
    def test_searchproduct(self):
        """"
        Searching for a particular product and verifying
        """
        self.sd.getMethodName(self.__class__.__name__)
        self.home_page.searchproduct("s")
        assert "samsung" in self.pl_page.verifysearchresult()
