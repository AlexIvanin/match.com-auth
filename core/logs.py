import logging
import colorlog
import time
import os,datetime

class Logs:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter('%(log_color)s%(levelname)s:%(name)s:%(message)s'))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    def start():
        dirName = datetime.datetime.now().strftime('%Y-%m-%d')
        issetDir = os.path.isdir("logs/" + dirName)
        if issetDir == False:
            os.makedirs("logs/" + dirName)
        logging.info("Program Started")
    def info(message):
        logging.info(message)
    def warning(message):
        logging.warning(message)
    def critical(message):
        logging.critical(message)
    def error(message):
        logging.error(message)
    def create_log(browser,login,password):
        dirName = datetime.datetime.now().strftime('%Y-%m-%d')
        issetDir = os.path.isdir("logs/" + dirName + '/' + login)
        if issetDir == False:
            os.makedirs("logs/" + dirName + '/' + login)
        browser.save_screenshot('logs/' + dirName + '/' + login + '/' + password +'.png')  
