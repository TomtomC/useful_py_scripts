import logging as l
import logging.config
import json
from pathlib import Path

"""
An attempt to provide a prepared logging module without writing out all the config code.
Results will be saved in the text file - see settings.json for settings
"""

# =======================CODE=======================
# base_path needed to prevent project from trying to find json file elsewhere.
# json file contains all the logging package settings.
# Adjust this file using the below 'logging config information' below.
base_path = Path(__file__).parent
file_path = (base_path / "settings.json").resolve()
with open(file_path, 'r') as f:
    config = json.load(f)

"""
logging config information:



"""

logging.config.dictConfig(config['module_settings']['logs'])

def log(log_type: str = "info",log_message: str = "") -> None:
    """
    invoke log(log_type,log_message) to create a log entry

    :param log_type: The log level you wish to trigger
    :param log_message: The message associated with the log level
    :return:
    """
    match log_type.lower():
        case "info":
            return l.info(log_message)
        case "warning":
            return l.warning(log_message)
        case "error":
            return l.error(log_message, exc_info=True)
        case "critical":
            return l.critical(log_message, exc_info=True)
        case "debug":
            return l.debug(log_message)
        case "": # if a blank entry is made
            return l.info(log_message)



# # # =======================TEST=======================
# def main() -> None:
#     log("info","Hello World")
#     log("warning","Hello World")
#     log("error","Hello World")
#     log("critical","Hello World")
#     log("debug","Hello World")
#
# if __name__ == '__main__':
#     main()