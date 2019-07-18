from pages.ActionBase import ActionBases
from test_case.function.ParceConfigLocator import ParceConfigLocator

class BookFlightTicket(ActionBases):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.parceLoc = ParceConfigLocator()
        self.LocSection = self.parceLoc.getSection('flight_ticket')

        self._homePage = self.LocSection['homePage'.lower()].split('>')
        self._flightTicket = self.LocSection['flightTicket'.lower()].split('>')
        self._double = self.LocSection['double'.lower()].split('>')
        self._fromCity = self.LocSection['fromCity'.lower()].split('>')
        self._toCity = self.LocSection['toCity'.lower()].split('>')
        self._fromDate = self.LocSection['fromDate'.lower()].split('>')
        self._returnDate = self.LocSection['returnDate'.lower()].split('>')
        self._hasChild = self.LocSection['hasChild'.lower()].split('>')
        self._hasBaby = self.LocSection['hasBaby'.lower()].split('>')
        self._submit = self.LocSection['submit'.lower()].split('>')

    def clickHomePage(self):
        self.getClick(*self._homePage)

    def clickFlightTicket(self):
        self.getClick(*self._flightTicket)

    def clickDouble(self):
        self.getClick(*self._double)

    def enterStartCity(self, startCity):
        self.getSendKeys(*self._fromCity, value=startCity)

    def enterToCity(self, toCity):
        self.getSendKeys(*self._toCity, value=toCity)

    def enterFromDate(self, fromDate):
        self.getSendKeys(*self._fromDate, value=fromDate)

    def enterReturnDate(self, returnDate):
        self.getSendKeys(*self._returnDate, value=returnDate)

    def clickHasChild(self):
        self.getClick(*self._hasChild)

    def clickHasBaby(self):
        self.getClick(*self._hasBaby)

    def clickToSearch(self):
        self.getClick(*self._submit)

    def performSearchFlightTicket(self, startCity, toCity, fromDate, returnDate):
        self.clickHomePage()
        self.getSleep(1)
        self.clickFlightTicket()
        self.clickDouble()
        self.getSleep(1)
        self.enterStartCity(startCity)
        self.enterToCity(toCity)
        self.getSleep(1)
        self.enterFromDate(fromDate)
        self.enterReturnDate(returnDate)
        self.getSleep(1)
        self.clickHasChild()
        self.clickHasBaby()
        self.clickToSearch()

    def veryfyTitle(self, title):
        return self.getAssertTitle(title)

    def veryfyPageSource(self, element):
        return self.getIsElementPresent(element)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    bft = BookFlightTicket(driver)
    bft.getUrl('https://www.ctrip.com')
    bft.performSearchFlightTicket('北京', '上海', '2019-07-29', '2019-07-31')
    result = bft.veryfyTitle('北京到上海')
    print(result)
    bft.getSleep(3)
    result = bft.veryfyPageSource('往返总价')
    print(result)
    bft.getClose()
