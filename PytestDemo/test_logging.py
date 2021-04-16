import logging
def test_loggingDemo():
# create object of logging class,name means which test case name will come in log
# if we will not give root will print in the place of test case name
   logger = logging.getLogger(__name__)

# logfile.log location will print log
   FileHandler = logging.FileHandler('logfile.log')

# which format log
   formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

# give format knowledge to filehandler
   FileHandler.setFormatter(formatter )

# here will add filehandler object
# here want to know where to print log and what format log
   logger.addHandler(FileHandler)

# if want to print only some specific level only
#set level
# we set level here info so only info,warning,error,critical will print debug will not print
   logger.setLevel(logging.INFO)


# order of level of log
   logger.debug("debug print")
   logger.info("info print")
   logger.warning("warning print")
   logger.error("error print")
   logger.critical("critical print")

