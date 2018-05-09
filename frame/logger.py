# -*- coding: utf8 -*-
import os
import ntpath
import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler


FORMATTER = logging.Formatter(
    "%(asctime)s - %(process)d - %(name)s - %(funcName)s - "
    "%(lineno)d - %(levelname)s - %(message)s")
FILEPATH = "/tmp/ninja/ninja.log"


def get_logger(logname="logger", loglevel=logging.INFO, logfile=FILEPATH):

    logger = logging.getLogger(logname)
    logger.setLevel(loglevel)

    # create file handler
    if not os.path.exists(logfile):
        os.mkdir(ntpath.dirname(logfile))

    file_handler = RotatingFileHandler(logfile)
    file_handler.setFormatter(FORMATTER)
    logger.addHandler(file_handler)

    # create console handler
    console_handler = StreamHandler()
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)

    return logger


log = get_logger()
