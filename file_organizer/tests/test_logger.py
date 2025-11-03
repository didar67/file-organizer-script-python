"""
Unit tests for logger setup and configuration.
"""

import logging
import os
from core.logger import setup_logger, get_logger

def test_setup_logger_creates_log_file(tmp_path):
    """Ensure log file is created successfully."""
    log_file = tmp_path / "test_log.log"
    logger = setup_logger(log_level=logging.INFO, log_file=str(log_file))
    logger.info("Testing log write")
    assert log_file.exists()

def test_get_logger_returns_logger_instance():
    """Ensure get_logger() returns a Logger object."""
    logger = get_logger()
    assert isinstance(logger, logging.Logger)
    logger.info("Logger retrieved successfully.")
