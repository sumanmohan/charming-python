__author__ = 'sumanrajmohan'

import logging

def setup_custom_logger(name):

    logPath = 'out/'
    fileName = 'simple_log'

    logFormatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(logFormatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)

    return logger