#encoding = utf-8
from selenium import webdriver

# driver实例
def getDriver():
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    # driver = webdriver.Edge()
    return driver