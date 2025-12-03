"""
This module sets up and manages application-wide logging using Python's 
built-in `logging` module. It ensures that all logs are consistently 
formatted, rotated, and safely written to disk.
"""

import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logger(log_level: int = logging.INFO, verbose: bool = False, log_file: str = "file_organizer.log") -> logging.Logger:
    """
    Configure and return a logger instance with rotating log file support.

    Args:
        log_level (int): The logging level (e.g., logging.INFO).
        verbose (bool): If True, enable console logging.
        log_file (str): The filename (with path) where logs will be written.

    Returns:
        logging.Logger: Configured logger instance.
    """

    # Ensure the log directory exists (create if missing)
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Create a custom logger
    logger = logging.getLogger("file_organizer")

    # Prevent duplicate handlers during re-import or multiple calls
    if not logger.hasHandlers():
        logger.setLevel(log_level)

        # Create rotating file handler (5 files, 1MB each)
        handler = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=5)

        # Set formatter for detailed logs
        formatter = logging.Formatter(
            "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
        )
        handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(handler)

        # Add console handler if verbose
        if verbose:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        logger.info("Logger initialized successfully.")

    return logger


def get_logger(log_level: int = logging.INFO, verbose: bool = False, log_file: str = "file_organizer.log") -> logging.Logger:
    """
    Get a configured logger instance.

    Args:
        log_level (int): The logging level (e.g., logging.INFO).
        verbose (bool): If True, enable console logging.
        log_file (str): The filename (with path) where logs will be written.

    Returns:
        logging.Logger: Configured logger instance.
    """
    return setup_logger(log_level, verbose, log_file)


# If this module runs directly (for quick test)
if __name__ == "__main__":
    log = setup_logger()
    log.info("Logger test message — working fine!")
