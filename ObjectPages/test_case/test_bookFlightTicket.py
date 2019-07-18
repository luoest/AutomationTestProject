from test_case.pages.BookFlightTicket import BookFlightTicket
from test_case.function.myunit import StartEnd
from test_case.function.myfunc import getScreenshot

# 测试查询机票全部流程，通过页面标题以及页面元素判断是否执行成功。
class BookFlightTicketTests(StartEnd):

    def test_valid_book(self):
        try:
            bft = BookFlightTicket(self.driver)
            bft.getUrl('https://www.ctrip.com')
            bft.performSearchFlightTicket('北京', '上海', '2019-07-29', '2019-07-30')
            result = bft.veryfyTitle('北京到上海')
            print('页面标题中是否出现元素“北京到上海”：',result)
            assert result == True
            bft.getSleep(5)
            result = bft.veryfyPageSource('往返总价')
            print('页面代码中是否出现元素“往返总价”：',result)
            assert result == True
        except Exception as e:
            getScreenshot(self.driver)
            raise e


        