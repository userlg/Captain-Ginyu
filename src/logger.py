"""Logging configuration for Captain Ginyu Script."""

import logging
import sys
from logging.handlers import RotatingFileHandler

from src.config import get_config


def setup_logger(
    name: str = "captain_ginyu",
    log_file: str | None = None,
    level: str | None = None,
) -> logging.Logger:
    """Configure and return a logger instance.

    Args:
        name: Logger name.
        log_file: Path to log file. If None, uses config default.
        level: Logging level. If None, uses config default.

    Returns:
        logging.Logger: Configured logger instance.
    """
    config = get_config()

    # Determine log level
    log_level = level or config.log_level
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(numeric_level)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # Create formatters
    detailed_formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    simple_formatter = logging.Formatter(fmt="%(levelname)s - %(message)s")

    # Console handler (INFO and above)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    logger.addHandler(console_handler)

    # File handler (DEBUG and above)
    if log_file is None:
        log_file = config.log_file

    try:
        file_handler = RotatingFileHandler(
            filename=log_file,
            maxBytes=config.log_max_bytes,
            backupCount=config.log_backup_count,
            encoding="utf-8",
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(detailed_formatter)
        logger.addHandler(file_handler)
    except (OSError, PermissionError) as e:
        logger.warning(f"Could not create log file {log_file}: {e}")

    return logger


def get_logger(name: str = "captain_ginyu") -> logging.Logger:
    """Get or create a logger instance.

    Args:
        name: Logger name.

    Returns:
        logging.Logger: Logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        return setup_logger(name)
    return logger
