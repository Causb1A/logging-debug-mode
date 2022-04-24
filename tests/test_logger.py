import logging
import pytest
from logger import Logger


@pytest.fixture
def logger_class_instance():
    """
    Logger class instance fixture
    """
    return Logger()


@pytest.fixture
def logger_class_instance2():
    """
    Second logging class instance fixture to test singleton feature
    """
    return Logger()


@pytest.fixture
def logging_module_instance():
    """
    Getting logging module instance to test other functions
    """
    return Logger().get_logger("test")


@pytest.fixture
def example_file_handler():
    """
    Created random file handler instance with same name to test add_handler functionality
    """
    filehandler = logging.FileHandler("test.log")
    filehandler.name = "fileHandler"
    return filehandler


def test_singleton_logger_class(logger_class_instance, logger_class_instance2):
    """
    test to check that the singleton class object is the same if instantiated a
    second time
    """
    c1 = logger_class_instance
    c2 = logger_class_instance2
    assert c1 == c2


def test_singleton_logger_class_object(logger_class_instance, logger_class_instance2):
    """
    test to check that logger singleton classes are the same despite chanigng self.debug_mode
    """
    c1 = logger_class_instance
    c2 = logger_class_instance2
    # Changing one of the objects in c2
    c2.log_file = "log_file_change.log"
    assert c1 == c2


def test_get_console_handler(logger_class_instance):
    """
    Testing naming feature of get console handler as a way to make sure it works
    """
    expected_console_name = "consoleHandler"
    console_handler = logger_class_instance.get_console_handler()
    assert expected_console_name == console_handler.name


def test_get_file_handler(logger_class_instance):
    """
    Testing naming feature of get file handler as a way to make sure it works
    """
    expected_file_name = "fileHandler"
    file_handler = logger_class_instance.get_file_handler()
    assert expected_file_name == file_handler.name


def test_get_logger(logging_module_instance):
    """
    Testing the right features of the logging module instance from get logger
    We should have 2 handlers, the file and console handler as well as the log
    level being at info level, which according to logging documentation is equivalent to 20
    """
    log = logging_module_instance
    expected_handler_numbers = 2
    result_handler_numbers = len(log.handlers)

    # We expect logging level to be 0 as we do not assign any logging level to the child handlers.
    expected_logging_level = 0
    result_logging_level = log.level

    assert expected_handler_numbers == result_handler_numbers
    assert expected_logging_level == result_logging_level


def test_add_handlers(
    logger_class_instance, logging_module_instance, example_file_handler
):
    """
    Testing the add handlers by attempting to add a handler with the same name, this
    shouldnt happen so handler number should remain at 2
    """
    # Attempt to add a handler with same name existing
    logger_class_instance.add_handlers(logging_module_instance, [example_file_handler])
    # Checking if handlers still 2
    assert len(logging_module_instance.handlers) == 2
