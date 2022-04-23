from logger import Logger
from .module_2 import does_something_module_2

logger = Logger()
log = logger.get_logger(__name__)


def function_initiates_debug_mode():
    """I am a function that initiates debug mode"""
    # Must be global as log is global in the file
    global log
    # Initiate the debug mode to be true
    logger.init_debug_mode(True)
    # reinitiates global log after setting debug_mode to be true
    log = logger.get_logger(__name__)


def does_something():
    print("Does Something Module 1")
    log.info("does something info module 1")
    log.debug("This is a DEBUG output module 1")


def run():
    # This should output some logs but Not the debug mode only INFO
    does_something()
    # lets try module 2
    does_something_module_2()
    # still no debug - ONLY INFO

    # Now I'm going to set debug mode to be true - FUNCTION THAT CHANGES THE SINGLETON CLASS AND LOG
    function_initiates_debug_mode()

    # Let's run the function does_something() again to see that debug will now be outputted. Debug is outputted here, great this is what I want
    does_something()

    # how about module 2 - DEBUG IS NOT OUTPUTTED HERE. I want this outputted with DEBUG.
    does_something_module_2()

    # Debug mode is created with one class singleton instance, you can change the variables on the fly. initialising debug mode.
