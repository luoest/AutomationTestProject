import logging
import logging.handlers
import inspect
from test_case.function.myfunc import logDirPATH

# 写入日志
def customLogger(logLevel = logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(logDirPATH + "/mylog.log", 'w', encoding='utf-8')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger