import inspect
import logging


class Baseclass:
    import logging
    def getlogger(self):
        # create object of logging class,name means which test case name will come in log
        # if we will not give root will print in the place of test case name
        # 1st line code will help to print the python file name
        loggerName=inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # logfile.log location will print log
        FileHandler = logging.FileHandler('logfile.log')

        # which format log
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        # give format knowledge to filehandler
        FileHandler.setFormatter(formatter)

        # here will add filehandler object
        # here want to know where to print log and what format log
        logger.addHandler(FileHandler)

        # if want to print only some specific level only
        # set level
        # we set level here info so only info,warning,error,critical will print debug will not print
        logger.setLevel(logging.DEBUG)
        return logger

