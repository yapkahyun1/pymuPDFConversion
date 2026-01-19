import datetime
import logging
import os
import sys
dateNow = datetime.datetime.now()


#logging.basicConfig(filename=dateNow.strftime("%Y-%m-%d_%H%M%S") + "-pdfConvert_logs.txt", level=logging.INFO)




def start_loggers():
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    logs_folder = os.path.join(script_dir + "Conversion_Logs")
    if not os.path.exists(logs_folder):
        logging.debug("Conversion Logs folder doesnt exists................Proceed to create one now")
        os.makedirs(logs_folder)
        logging.debug("Conversion Logs folder created, will begun storing the logs in this folder")
    else:
        logging.debug("Conversion Logs folder exists, will begun storing the logs in this folde")

    log_filename = f"{dateNow.strftime('%Y-%m-%d_%H%M%S')}_pdfConvert_logs.txt"
    logging.basicConfig(filename=log_filename, level=logging.DEBUG, format="[%(levelname)s] %(message)s")
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


