import logging

import structlog


def setup_logger():
    # TODO: configure logger using settings

    logging.config.dictConfig({
            "version": 1,
            "disable_existing_loggers": False,
            "handlers": {
                "default": {
                    "level": "DEBUG",
                    "class": "logging.StreamHandler",
                },
                "file": {
                    "level": "DEBUG",
                    "class": "logging.handlers.WatchedFileHandler",
                    "filename": "/logs/fastapi.log",  # TODO: expose
                },
            },
            "loggers": {
                "": {
                    "handlers": ["default", "file"],
                    "level": "DEBUG",
                    "propagate": True,
                },
            }
    })
    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            # structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            # structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
            structlog.processors.JSONRenderer(),
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        # wrapper_class=structlog.stdlib.BoundLogger,
        # cache_logger_on_first_use=True,
    )
    structlog.get_logger("log").info("Logger configured")
    return structlog.get_logger()





    # logger.setLevel(logging.INFO)

    # # configure formatter for logger
    # formatter = logging.Formatter(LOG_FORMAT)

    # # configure console handler
    # console = logging.StreamHandler()
    # console.setFormatter(formatter)

    # # configure rotating file handler
    # # TODO: expose path
    # file = logging.handlers.RotatingFileHandler(
    #     filename="/logs/fastapi.log", mode="a", maxBytes=15000000, backupCount=5
    # )
    # file.setFormatter(formatter)

    # # add handlers
    # logger.addHandler(console)
    # logger.addHandler(file)

    # # logging.basicConfig(level=logging.INFO)
    # structlog.configure(
    #     processors=[
    #         structlog.stdlib.add_log_level,
    #         structlog.processors.TimeStamper(fmt="iso"),
    #         structlog.processors.format_exc_info,
    #         structlog.processors.JSONRenderer(),
    #     ],
    # )
    # return logger


log = setup_logger()
