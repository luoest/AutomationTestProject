import os
import time

# 获取常用地址
test_reportPATH = ''
configLocPATH = ''
logDirPATH = ''
base_path = ''
nOW = ''
currentPicDir = ''
def getPath():
    global test_reportPATH, configLocPATH, logDirPATH, base_path, nOW, currentPicDir
    base_path = os.path.dirname(__file__)
    base_path = str(base_path).replace('\\', '/').split('/ObjectPages')[0]
    test_reportPATH = base_path + '/ObjectPages/test_report'
    configLocPATH = base_path + '/ObjectPages/config/PageElementLocator.ini'
    logDirPATH = base_path + '/ObjectPages/logs'
    nOW = time.strftime('%Y-%m-%d %H-%M-%S')
    screenshotDir = base_path + '/ObjectPages/exceptionPic'
    currentPicDir = screenshotDir + '/' + nOW
    if not os.path.exists(screenshotDir):
        os.mkdir(screenshotDir)

    # 每次执行都生成新的异常文件夹，以示区分
    if not os.path.exists(currentPicDir):
        os.mkdir(currentPicDir)
getPath()

# 异常截图到指定文件夹，每次执行生成新的文件夹
def getScreenshot(driver):
    imageName = currentPicDir + '/' + str(int(time.time()*1000)) + '.png'
    print('异常情况截图地址：'+ str(imageName))
    driver.get_screenshot_as_file(imageName)
    return imageName


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    try:
        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').send_keys(2019)
        getScreenshot(driver)
        driver.find_element_by_id('su').click()
        getScreenshot(driver)
        time.sleep(1)
        driver.find_element_by_partial_link_text('百度百科').click()
        time.sleep(1)
        getScreenshot(driver)
    finally:
        driver.quit()


