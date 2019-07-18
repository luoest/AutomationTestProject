import unittest
import time
from test_case.function.BSTestRunner import BSTestRunner
from test_case.function.myfunc import test_reportPATH, logDirPATH
import os

# BSTestRunner 为第三方模块，已根据需要将其中的unicode’ 换成 ‘str’
test_case = './'
discover = unittest.defaultTestLoader.discover(test_case, 'test_bookFlightTicket.py')

now = time.strftime('%Y-%m-%d %H-%M-%S')
reportName = test_reportPATH + '/' + now + ' report.html'
with open(reportName, 'w', encoding='utf-8') as f:
    runner = BSTestRunner(stream=f, title='自动化测试案例', verbosity=2, description='python+selenium自动化测试携程查询机票流程')
    runner.run(discover)
    f.close()

latest_report = test_reportPATH + '/' + now + ' report.html'
os.startfile(latest_report)


