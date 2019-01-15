from FrameWork.pom.HomePage import HomePage
from FrameWork.pom.PL_Page import PL_Page
from FrameWork.pom.PDP import PD_Page

import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp","getStatus")
class Test_VerifyShipmentCharge(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.home_page = HomePage(self.driver)
        self.pl_page = PL_Page(self.driver)
        self.pdp = PD_Page(self.driver)

    @pytest.mark.run(order=1)
    def test_gotocart(self):
        self.home_page.searchproduct()
        self.pl_page.productLists(4)
        self.pdp.addtocart()