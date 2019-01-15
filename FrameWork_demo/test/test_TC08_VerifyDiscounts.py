from FrameWork.pom.HomePage import HomePage
from FrameWork.pom.PL_Page import PL_Page

import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp","getStatus")
class Test_VerifyDiscount(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.home_page = HomePage(self.driver)
        self.pl_page = PL_Page(self.driver)

    @pytest.mark.run(order=1)
    def test_discounts(self):
        """
        It verifies whether discount is proper
        :return: None
        """
        self.home_page.searchproduct()
        self.pl_page.clickonleftnav()
        price=self.pl_page.stringtolist(self.pl_page.productdiscounts())
        for i in price:
            assert int(i) > 50, print("less than 50%")
            print("more than 50%")

