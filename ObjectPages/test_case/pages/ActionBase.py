from pages.ObjectMap import ObjectMaping
import os
from test_case.function.customLogger import customLogger
import time

class ActionBases(ObjectMaping):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cl = customLogger()

    def getClear(self, *locSet):
        try:
            self.getElement(*locSet)
            msg = '执行清空操作。'
            print(msg)
            self.cl.info(msg)
        except Exception as e:
            raise e

    def getSendKeys(self, *locSet, value):
        try:
            self.getElement(*locSet).send_keys(value)
            msg = '发送信息：' + str(value)
            print(msg)
            self.cl.info(msg)
        except Exception as e:
            raise e

    def getClick(self, *locSet):
        try:
            self.getElement(*locSet).click()
            msg = '执行点击操作。'
            print(msg)
            self.cl.info(msg)
        except Exception as e:
            raise e

    def getSleep(self, sleepSeconds):
        time.sleep(sleepSeconds)

    def getClose(self):
        try:
            self.driver.quit()
            msg = '关闭浏览器。'
            print(msg)
            self.cl.info(msg)
        except Exception as e:
            raise e

    def getTitle(self):
        return self.driver.title

    def getAssertTitle(self, titleElement):
        try:
            assert str(titleElement) in self.getTitle(), '页面标题中没有发现元素：' + str(titleElement)
            return True
        except Exception as e:
            print(e)
            self.cl.debug(e)
            return False

    def getPageSource(self):
        return self.driver.page_source

    def getIsElementPresent(self, element):
        try:
            assert str(element) in self.getPageSource(), '页面代码中没有发现目标元素：' + str(element)
            return True
        except Exception as e:
            print(e)
            self.cl.debug(e)
            return False

