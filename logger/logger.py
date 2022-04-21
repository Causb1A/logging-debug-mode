import logging
import sys
from logging import handlers


class Logger:
    """
    Singleton Logger class. This class is only instantiated ONCE
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.debug_mode = True
            cls.formatter = logging.Formatter(
                "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
            )
            cls.log_file = "cap_emr_launcher.log"
            cls.debug_mode = False

        return cls._instance

    def get_console_handler(self):
        """Defines a console handler to come out on the console

        Returns:
            logging handler object : the console handler
        """
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def get_file_handler(self):
        """Defines a file handler to come out on the console

        Returns:
            logging handler object : the console handler
        """
        file_handler = handlers.RotatingFileHandler(self.log_file, maxBytes=2000)
        file_handler.setFormatter(self.formatter)
        return file_handler

    def init_debug_mode(self, option: bool):
        """initiates debug mode when initiated by user

        Args:
            option (bool): Boolean true or false, if debug mode is true it will assign self.debug to true
        """
        self.debug_mode = option

    def new_log_location(self, log_location: str):
        """Reassigns new log location

        Args:
            log_location (str): log location for logs
        """
        self.log_file = log_location

    def get_logger(self, logger_name: str):
        """Generates logger for use in the modules

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
        logger.addHandler(self.get_console_handler())
        logger.addHandler(self.get_file_handler())
        logger.propagate = False
        return logger
