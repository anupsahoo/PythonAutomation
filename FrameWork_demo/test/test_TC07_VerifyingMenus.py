from FrameWork.pom.HomePage import HomePage

import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp","getStatus")
class Test_VerifyMenuElements(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.home_page = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def test_descending(self):
        """"
         searching for products based on descending price and validating the sort
        """
        actual=self.home_page.shopbycategorymenus()
        expected=self.home_page.readlinebyline()
        for i in expected:
            assert i in actual

