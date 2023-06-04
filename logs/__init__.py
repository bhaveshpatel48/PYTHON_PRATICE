from .config import *
import logging
from logging import config

# Configure logging using the dictionary settings
config.dictConfig(LOGGER_SETTINGS)

# Create a logger and log some messages
logger = logging.getLogger(__name__)
logger.info("Logging Configuration loaded successfully !!!")