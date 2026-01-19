import datetime
import logging

dateNow = datetime.datetime.now()


#logging.basicConfig(filename=dateNow.strftime("%Y-%m-%d_%H%M%S") + "-pdfConvert_logs.txt", level=logging.INFO)




def start_loggers():
    logging.basicConfig(filename=dateNow.strftime("%Y-%m-%d_%H%M%S") + "-pdfConvert_logs.txt", level=logging.DEBUG, format="[%(levelname)s] %(message)s")
    #logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] %(message)s")



def log_info(debugMessages):
    getTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(getTimeStamp + " - " + debugMessages)




def log_debug(debugMessages):
    getTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.debug(getTimeStamp + " - " + debugMessages)




def log_error(debugMessages):
    getTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.error(getTimeStamp + " - " + debugMessages)




def log_critical(debugMessages):
    getTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.critical(getTimeStamp + " - " + debugMessages)


def log_warning(debugMessages):
    getTimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.warning(getTimeStamp + " - " + debugMessages)


