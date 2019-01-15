from FrameWork.pom.HomePage import HomePage
from FrameWork.pom.PL_Page import PL_Page
from FrameWork.pom.PDP import PD_Page

import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp","getStatus")
class Test_stock(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.home_page = HomePage(self.driver)
        self.pl_page = PL_Page(self.driver)
        self.pd_page = PD_Page(self.driver)

    @pytest.mark.run(order=1)
    def test_verifystock(self):
        """
        verifying the product's availability
        """
        self.home_page.searchproduct()
        self.pl_page.productLists(3)
        available=self.pd_page.stockAvailabilty()
        assert "In" in available, print("Out of Stock")
        print("In stock")
