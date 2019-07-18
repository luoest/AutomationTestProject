from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_case.function.customLogger import customLogger
import logging

class ObjectMaping(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeOut = 10
        self.wait = WebDriverWait(self.driver, self.timeOut)
        self.cl = customLogger()

    def getUrl(self, url):
        self.driver.get(url)

    def getElement(self, *locSet):
        try:
            element = self.wait.until(lambda driver: driver.find_element(*locSet))
            msg = '发现元素，定位套件为：' + str(locSet)
            self.cl.info(msg)
            print(msg)
            return element
        except Exception as e:
            raise e

    def getPresentElement(self, *locSet):
        try:
            element = self.wait.until(EC.presence_of_element_located((locSet)))
            msg = '发现元素，定位套件为：' + str(locSet)
            self.cl.info(msg)
            print(msg)
            return element
        except Exception as e:
            raise e

    def getVisibleElement(self, *locSet):
        try:
            element = self.wait.until(EC.visibility_of_element_located((locSet)))
            msg = '发现元素，定位套件为：' + str(locSet)
            self.cl.info(msg)
            print(msg)
            return element
        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_option = Options()
    chrome_option.add_argument('--start-maximized')
    chrome_option.add_argument('--disable-extensions')
    driver = webdriver.Chrome(options=chrome_option)


    om = ObjectMaping(driver)
    om.getUrl('https://www.baidu.com')
    om.getElement('id', 'kw').send_keys('python')
    om.getPresentElement('id', 'su').click()

