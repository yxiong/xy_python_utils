#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Dec 04, 2015.

import logging
import sys

class DebugOrInfoFilter(logging.Filter):
    """Keep the record only if the level is debug or info."""
    def filter(self, record):
        return record.levelno in (logging.DEBUG, logging.INFO)

def config_logger(logger, formatter):
    """Configure the logger such that debug and info messages are directed to stdout,
    while more critical warnings and errors to stderr.
    """
    stdoutHandler = logging.StreamHandler(sys.stdout)
    stdoutHandler.setLevel(logging.DEBUG)
    stdoutHandler.setFormatter(formatter)
    stdoutHandler.addFilter(DebugOrInfoFilter())
    logger.addHandler(stdoutHandler)

    stderrHandler = logging.StreamHandler(sys.stderr)
    stderrHandler.setLevel(logging.WARNING)
    stderrHandler.setFormatter(formatter)
    logger.addHandler(stderrHandler)

if __name__ == "__main__":
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    log_format = '%(asctime)s.%(msecs)03d\t%(process)d\t%(filename)s:%(lineno)s\t%(funcName)s\t%(message)s'
    formatter = logging.Formatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")
    config_logger(logging.getLogger(), formatter)

    # To stdout.
    logging.debug("debug")
    logging.info("info")

    # To stderr.
    logging.warning("warning")
    logging.error("error")
