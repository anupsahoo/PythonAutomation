from FrameWork.pom.HomePage import HomePage
from FrameWork.pom.PL_Page import PL_Page

import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp","getStatus")
class Test_navigate(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.home_page = HomePage(self.driver)
        self.pl_page = PL_Page(self.driver)

    @pytest.mark.run(order=1)
    def test_searchproduct(self):
        """
        verifying the navigation option for multi page
        """
        self.home_page.searchproduct()
        #self.pl_page.scrolltobottom()
        self.pl_page.previousnavigator()
        self.pl_page.nextnavigator()
        assert "Previous" in self.pl_page.previousnavigate
        assert "Next" in self.pl_page.nextnavigate
        self.pl_page.gotonext()
        second=self.pl_page.pageSelectionstatus(2)
        assert second == True, print("page not navigated to next")
        print("page navigated to next page")
