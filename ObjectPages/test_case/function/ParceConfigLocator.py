from configparser import ConfigParser
from test_case.function.myfunc import configLocPATH
'''
将页面元素保存在PageElementLocator.ini中，方便统一管理。
格式为：元素=定位方式>定位器
通过字典方法，将其一一对应。调用时，通过split('>')，分离定位方式和定位器
'''
class ParceConfigLocator():
    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read(configLocPATH, encoding='utf-8')

    def getSection(self, section):
        sectionValue = dict(self.parser.items(section))
        return sectionValue

    def getValue(self, section, value):
        return self.parser.get(section, value)


if __name__ == '__main__':
    pcl = ParceConfigLocator()
    print(pcl.getSection('flight_ticket'))
    print(pcl.getValue('flight_ticket', 'double'))
