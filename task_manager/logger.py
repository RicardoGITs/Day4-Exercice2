import logging
import os

def setup_logger(log_file="logs/task_manager.log"):
    if not os.path.exists("logs"):
        os.makedirs("logs")
    logger = logging.getLogger("task_manager")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
