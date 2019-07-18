from DriverBase.DriverBase import getDriver
import unittest

# 起始和结束
class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = getDriver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
