from FrameWork.pom.PL_Page import PL_Page
from FrameWork.pom.HomePage import HomePage
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp","getStatus")
class Test_search(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self,oneTimeSetUp):
        self.pl_page = PL_Page(self.driver)
        self.home_page = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def test_sortoptions(self):
        """
        Select the product based on filter options
        """
        self.home_page.searchproduct()
        self.pl_page.sortoptions()