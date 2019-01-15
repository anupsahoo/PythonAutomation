import pytest
import xlrd
from FrameWork.base.Extended_Webdriver import Extended_Webdriver
from FrameWork.CustomExceptions.StatusException import StatusFailException
from FrameWork.pom.HomePage import HomePage
from FrameWork.base.Selenium_driver import SeleniumDriver
import os.path

@pytest.fixture()
def setUp(request):
    print("Running method level setUp")
    # failed_before = request.session._testsfailed
    yield
    SeleniumDriver(request.cls.driver).get_screenshot()
    print("Running method level tearDown")



@pytest.fixture(scope="class")
def getStatus():
    my_path=os.path.abspath(os.path.dirname(__file__))
    _excelfilepath = os.path.join(my_path,"../DataFiles/TestData.xlsx")
    book = xlrd.open_workbook(_excelfilepath)
    runmode = book.sheet_by_index(0).cell(1, 1).value
    if runmode == "N":
        raise StatusFailException
    else:
        pass

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    EW = Extended_Webdriver(browser)
    driver = EW.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="function")
def login(request):
    home_page = HomePage(request.cls.driver)
    home_page.login("user","pwd")
    yield
    home_page.logout()
    assert "Sign In" in request.cls.driver.title


