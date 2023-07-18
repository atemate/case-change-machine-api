import logging
from pathlib import Path

import ecs_logging  # logging in elastic-compatible format 

from .settings import SETTINGS


def setup_logger(log_file: str | None = None) -> logging.Logger:
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)

    handlers: list[logging.Handler] = [
        logging.StreamHandler(),
    ]
    if log_file:
        Path(log_file).parent.mkdir(exist_ok=True, parents=True)
        handlers.append(logging.FileHandler(filename=log_file))

    for handler in handlers:
        handler.setFormatter(ecs_logging.StdlibFormatter())
        logger.addHandler(handler)

    return logger


log = setup_logger(SETTINGS["server"].log_file)
