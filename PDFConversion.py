# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pymupdf
import sys
import loggers





# print("Index 2: ", sys.argv[1])
#
#
#
# #Path = "C:\\Users\\HP\\OneDrive\\Desktop\\PAMB\\PolicyContract.pdf"
Path = sys.argv[1]
#OutputPath = "C:\\Users\\HP\\OneDrive\\Desktop\\PAMB\\ExtractedTxt.txt"
OutputPath = sys.argv[2]
#
#
# logging.basicConfig(level=logging.DEBUG)
#
# logging.debug("DEBUG LOGS")
# logging.critical("CRITICAL LOGS")
#
#

#
doc = pymupdf.open(Path)
txtOutput = open(OutputPath, "wb")


for page in doc: # iterate the document pages
    text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
    txtOutput.write(text) # write text of page
    txtOutput.write(bytes((12,))) # write page delimiter (form feed 0x0C)
txtOutput.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
