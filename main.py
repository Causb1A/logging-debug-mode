from my_app import module_1
import sys
from logger import Logger
import logging

# Starts logger for file
log = Logger().get_logger(__name__)
# This sets the root logger level to be info.
logging.root.setLevel(logging.INFO)

if __name__ == "__main__":
    try:
        module_1.run()
    except:
        log.error("Put error here or print your traceback")
        sys.exit(1)
