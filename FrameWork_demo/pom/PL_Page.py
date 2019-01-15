from FrameWork.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select
import time

class PL_Page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    #locators
    _brand = "//span[@class='a-label a-checkbox-label']/span[text()='HP']"
    _price = "//span[contains(text(),'30,000')]"
    _ratings = "//span[text()='3 Stars & Up']"
    _product = "//span/span[@class='a-color-state a-text-bold']"
    _sortbyarrow = "sort"
    _productprices = "//div[@class='a-row a-spacing-none']/..//a[@class='a-link-normal a-text-normal']" + \
                   "/span[@class='a-size-base a-color-price s-price a-text-bold' or " + \
                   "@class='a-size-base a-color-price a-text-bold']"
    _singleselect="Price: Low to High"
    _descselect="Price: High to Low"
    _produtstext="//a/h2"
    _previousnavigator="//div[@id='bottomBar']//span[@id='pagnPrevString']"
    _nextnavigator="//div[@id='bottomBar']//span[@id='pagnNextString']"
    _firstpage="//div[@id='bottomBar']//span[text()='1']"
    _secondpage = "//div[@id='bottomBar']//span[text()='2']"
    _menclothing="//div[id='leftNavContainer']//a/span[text()='"+"Men's Clothing"+"']"
    _offprice="//div[id='leftNavContainer']//a/span[text()='50% Off or more']"
    _discounts="//div/div[@class='a-row a-spacing-none']/div[@class='a-row a-spacing-none']" \
                        "/span[@class='a-size-small a-color-secondary a-text-strike']/following-sibling::span"

    #expected
    ascendingprice=[]
    descendingprice=[]
    previousnavigate=''
    nextnavigate=''


    def sortoptions(self):
        """
        for applying filtering options
        :return: None
        """
        self.waitForElement(self._brand, "xpath", 20, 0.5)
        self.elementClick(self._brand, "xpath")
        self.waitForElement(self._price, "xpath", 20, 0.5)
        self.elementClick(self._price, "xpath")
        self.waitForElement(self._ratings, "xpath", 20, 0.5)
        self.elementClick(self._ratings, "xpath")

    def clickonleftnav(self):
        """
        for applying filter options
        :return:
        """
        self.waitForElement(self._menclothing, "xpath", 20, 0.5)
        self.elementClick(self._menclothing, "xpath")
        self.waitForElement(self._offprice, "xpath", 20, 0.5)
        self.elementClick(self._offprice, "xpath")

    def verifysearchresult(self):
        self.waitForElement(self._product,"xpath",20,0.5)
        prodtext=self.getElement(self._product, "xpath").text
        return prodtext

    def ascendingsort(self):
        self.waitForElement(self._sortbyarrow, "id", 20, 0.5)
        self.elementClick(self._sortbyarrow, "id")
        sel=Select(self.getElement(self._sortbyarrow,"id"))
        sel.select_by_visible_text(self._singleselect)
        self.waitForElement(self._productprices, "xpath", 20, 0.5)
        prices=self.driver.find_elements(self.getByType("xpath"),self._productprices)
        all_prices=[x.text for x in prices]
        self.ascendingprice=sorted(all_prices)
        return all_prices

    def descendingsort(self):
        self.waitForElement(self._sortbyarrow, "id", 20, 0.5)
        self.elementClick(self._sortbyarrow, "id")
        sel=Select(self.getElement(self._sortbyarrow,"id"))
        sel.select_by_visible_text(self._descselect)
        self.waitForElement(self._productprices, "xpath", 20, 0.5)
        prices=self.driver.find_elements(self.getByType("xpath"),self._productprices)
        all_prices=[x.text for x in prices]
        self.descendingprice=sorted(all_prices)
        self.descendingprice.reverse()
        return all_prices

    def productLists(self,num):
        n=int(num)
        self.waitForElement(self._produtstext, "id", 20, 0.5)
        parent=self.driver.current_window_handle
        products = self.getElements(self._produtstext,"xpath")
        products[n].click()
        allwindows=self.driver.window_handles
        for i in allwindows:
            if i != parent:
                self.driver.switch_to.window(i)
        return True


    def productdiscounts(self):
        elem=self.getElements(self._discounts,"xpath")
        discountprices=[x.text for x in elem]
        return discountprices

    def stringtolist(self,list):
        numlist=[]
        for i in list:
            l=[j for j in i]
            s=''
            for k in l:
                if k.isdigit():
                    s=s+k
            numlist.append(s)
        return numlist

    def previousnavigator(self):
        self.previousnavigate=self.getElement(self._previousnavigator, "xpath").text

    def nextnavigator(self):
        self.nextnavigate = self.getElement(self._nextnavigator, "xpath").text

    def pageSelectionstatus(self,num):
        n=int(num)
        if n==1:
            self.waitForElement(self._firstpage, "id", 20, 0.5)
            return self.getElement(self._firstpage, "xpath").is_enabled()
        elif n==2:
            self.driver.set_page_load_timeout(30)
            return self.getElement(self._secondpage, "xpath").is_enabled()

    def gotonext(self):
        self.elementClick(self._nextnavigator, "xpath")

    def scrolltobottom(self):
        #self.getElement(self._previousnavigator, "xpath").location_once_scrolled_into_view
        self.driver.execute_script("arguments[0].scrollIntoView();", self.getElement(self._previousnavigator, "xpath"))





