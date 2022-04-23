import logging
import sys
from logging import handlers


class Logger:
    """
    Singleton Logger class. This class is only instantiated ONCE. It is to keep a consistent
    criteria for the logger throughout the application.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.debug_mode = True
            cls.formatter = logging.Formatter(
                "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
            )
            cls.log_file = "application_log_file.log"
            cls.debug_mode = False

        return cls._instance

    def get_console_handler(self):
        """Defines a console handler to come out on the console

        Returns:
            logging handler object : the console handler
        """
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        console_handler.name = "consoleHandler"
        return console_handler

    def get_file_handler(self):
        """Defines a file handler to come out on the console.

        Returns:
            logging handler object : the console handler
        """
        file_handler = handlers.RotatingFileHandler(self.log_file, maxBytes=5000)
        file_handler.setFormatter(self.formatter)
        file_handler.name = "fileHandler"
        return file_handler

    def add_handlers(self, logger, handler_list: list):
        """Adds handlers to the logger, checks first if handlers exist to avoid
        duplication

        Args:
            logger: Logger to check handlers
            handler_list: list of handlers to add
        """
        existing_handler_names = []
        for existing_handler in logger.handlers:
            existing_handler_names.append(existing_handler.name)

        for new_handler in handler_list:
            if new_handler.name not in existing_handler_names:
                logger.addHandler(new_handler)

    def init_debug_mode(self, option: bool):
        """initiates debug mode when initiated by user

        Args:
            option (bool): Boolean true or false, if debug mode is true it will assign self.debug to true
        """
        self.debug_mode = option

    def get_logger(self, logger_name: str):
        """Generates logger for use in the modules. Checks if debug mode is true and adds handler if doesnt exist.
        Args:
            logger_name (string): name of the logger

        Returns:
            logger: returns logger for module
        """
        logger = logging.getLogger(logger_name)
        if self.debug_mode is True:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)

        console_handler = self.get_console_handler()
        file_handler = self.get_file_handler()
        self.add_handlers(logger, [console_handler, file_handler])

        logger.propagate = False
        return logger
