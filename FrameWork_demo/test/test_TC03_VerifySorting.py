from FrameWork.pom.HomePage import HomePage
from FrameWork.pom.PL_Page import PL_Page

import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp","getStatus")
class Test_search(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.home_page = HomePage(self.driver)
        self.pl_page = PL_Page(self.driver)

    @pytest.mark.run(order=1)
    def test_ascending(self):
        """
         searching for products based on ascending price and validating the sort
        """
        self.home_page.searchproduct()
        assert self.pl_page.ascendingsort() == self.pl_page.ascendingprice
