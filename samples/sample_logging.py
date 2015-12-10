#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Dec 04, 2015.

import logging
import sys

from xy_python_utils.logging_utils import split_stdout_stderr

if __name__ == "__main__":
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    log_format = '%(asctime)s.%(msecs)03d\t%(process)d\t%(filename)s:%(lineno)s\t%(funcName)s\t%(message)s'
    formatter = logging.Formatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")
    split_stdout_stderr(root_logger, formatter)

    # To stdout.
    logging.debug("debug")
    logging.info("info")

    # To stderr.
    logging.warning("warning")
    logging.error("error")
