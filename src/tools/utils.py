import subprocess
import logging.handlers

logger = logging.getLogger()
LOG_FILE = "logs/tools.log"
hdlr = logging.handlers.TimedRotatingFileHandler(LOG_FILE, encoding='utf-8')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.NOTSET)


def loging(level='info', msg=''):
    if level == 'info':
        logging.info(msg)
    elif level == 'debug':
        logging.debug(msg)
    elif level == 'error':
        logging.error(msg)

