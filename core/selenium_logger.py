import logging
from logging.handlers import RotatingFileHandler

LOGGER_NAME = 'myapp'

def initialize_logger():
    logger = logging.getLogger(LOGGER_NAME)
    logFile = 'log.txt'
    hdlr = RotatingFileHandler(logFile, mode='a', maxBytes=1024, 
                             backupCount=2, encoding=None, delay=0)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

def remove_log_handler():
    logger = logging.getLogger(LOGGER_NAME)
    logger.handlers = []