import logging

import ecs_logging

from .settings import SETTINGS


def setup_logger(log_file: str):
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)

    handlers: list[logging.Handler] = [
        logging.FileHandler(filename=log_file),
        logging.StreamHandler(),
    ]
    for h in handlers:
        h.setFormatter(ecs_logging.StdlibFormatter())
        logger.addHandler(h)

    return logger


log = setup_logger(SETTINGS["server"].log_file)
