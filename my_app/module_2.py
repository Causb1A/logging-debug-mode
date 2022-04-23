from logger import Logger


def does_something_module_2():
    print("Does something module 2")
    Logger().logger(__name__).info("does something info module 2")
    Logger().logger(__name__).debug("This is a DEBUG output module 2")
