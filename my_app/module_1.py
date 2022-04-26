from logger import Logger
from .module_2 import does_something_module_2

log = Logger().get_logger(__name__)


def does_something():
    """I am a function that does something - my purpose is to test logging."""
    print("Does Something Module 1")
    log.info("does something info module 1")
    log.debug("This is a DEBUG output module 1")


def run():
    # This should output some logs but Not the debug mode only INFO - remember the child logger is inheriting from root logger
    does_something()
    # lets try module 2
    does_something_module_2()
    # still no debug - ONLY INFO

    # Now I'm going to set debug mode to be true - Function that changes root level logging. This could be from anything,
    # This could be from a user initiating --debug or its own function etc. Up to you.
    Logger().set_debug_mode(True)

    # Let's run the function does_something() again to see that debug will now be outputted. Debug is outputted here.
    does_something()

    # how about module 2 - Debug is also outputted here
    does_something_module_2()
