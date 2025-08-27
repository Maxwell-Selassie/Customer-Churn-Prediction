from log_setup import log_setup
import logging

# First, set up logging
log_setup("logging.yaml")

# Get a logger instance for this module
logger = logging.getLogger(__name__)

def main():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.error("This is an error message")

if __name__ == "__main__":
    main()
