# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pymupdf
import sys

import Loggers
from Loggers import *
import time



start_loggers()
# print("Index 2: ", sys.argv[1])
#
#


try:
    # #Path = "C:\\Users\\HP\\OneDrive\\Desktop\\PAMB\\PolicyContract.pdf"

    Path = sys.argv[1]
    Loggers.log_info("Current path for the file conversion: " + sys.argv[1])
    # OutputPath = "C:\\Users\\HP\\OneDrive\\Desktop\\PAMB\\ExtractedTxt.txt"
    OutputPath = sys.argv[2]
    Loggers.log_info("Current path for the output after conversion: " + sys.argv[2])
    Loggers.log_debug("Proceed to open the pdf file.....")
    doc = pymupdf.open(Path)
    Loggers.log_debug("PDF File opened....")


    Loggers.log_debug("New Text File created......")
    txtOutput = open(OutputPath, "wb")
    Loggers.log_debug("Text file is opened to write content")


    Loggers.log_debug("Begin the PDF Extraction")
    Loggers.log_debug("Total page counted: " + str(doc.page_count))
    for page in doc: # iterate the document pages
        current_page = page.number + 1  # human-readable (starts from 1)
        Loggers.log_debug(f"Extracting Page Number {str(current_page)}")
        text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
        txtOutput.write(text) # write text of page
        Loggers.log_debug(f"Content for Page Number {str(current_page)} is written")
        txtOutput.write(bytes((12,))) # write page delimiter (form feed 0x0C)
    txtOutput.close()
    Loggers.log_debug("File closed successfully")
    Loggers.log_debug("PDF has been converted to text sucessfully!")


except:
    Loggers.log_error("Invalid File Path for Input and output, please ensure the path is correct followed by the file extension .txt or .pdf")





#
#
# logging.basicConfig(level=logging.DEBUG)
#
# logging.debug("DEBUG LOGS")
# logging.critical("CRITICAL LOGS")
#
#

#



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
