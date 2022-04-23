from my_app import module_1
import traceback
import sys
from logger import Logger

log = Logger().get_logger(__name__)

if __name__ == "__main__":
    try:
        module_1.run()
    except:
        log.error("Put error here or print your traceback")
        sys.exit(1)
