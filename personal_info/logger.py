#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logging.handlers

import coloredlogs

# TODO:
# Push this to a separate library that can take a logger name and
# return a logger.

logger = logging.getLogger("personal_info")
logger.setLevel(logging.DEBUG)

coloredlogs.install(level="DEBUG", logger=logger)


fh_fmt = (
    "%(asctime)s - [%(levelname)s] [%(name)s] "
    "[%(filename)s:%(lineno)s - %(funcName)s()] "
    "%(message)s")
fh_formatter = logging.Formatter(fh_fmt)
fh = logging.handlers.RotatingFileHandler(
    'product_viewer.log', maxBytes=1024*1024, backupCount=10)
fh.setLevel(logging.DEBUG)
fh.setFormatter(fh_formatter)
logger.addHandler(fh)

# add ch to logger
logger.debug("Created logger.")


def install_logger(application):
    """Installs logger on flask and werkzeug objects."""
    import logging
    import logging.handlers
    import coloredlogs
    logging.getLogger("werkzeug").setLevel(logging.DEBUG)
    logging.getLogger("werkzeug").addHandler(fh)
    application.logger.setLevel(logging.DEBUG)
    request_fh_fmt = (
        "%(asctime)s - [%(levelname)s] [%(name)s] "
        "[%(filename)s:%(lineno)s - %(funcName)s()] "
        "%(message)s")
    request_fh_formatter = logging.Formatter(request_fh_fmt)
    request_fh = logging.handlers.RotatingFileHandler(
        'werkzeug_requests.log', maxBytes=1024*1024, backupCount=10)
    request_fh.setLevel(logging.DEBUG)
    request_fh.setFormatter(request_fh_formatter)
    application.logger.addHandler(request_fh)
    coloredlogs.install(level="DEBUG", logger=application.logger)
    coloredlogs.install(level="DEBUG", logger=logging.getLogger("personal_info"))
