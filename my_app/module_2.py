from logger import Logger
from logger import logging

log = Logger().get_logger(__name__)


def does_something_module_2():
    print("Does something module 2")
    log.info("logging info in module 2")
    log.debug("This is a DEBUG output in module 2")
