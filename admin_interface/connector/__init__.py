import logging
LOG_FILENAME = 'responsetime.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
logging.debug('This message should go to the log file')