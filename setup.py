#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Dec 09, 2014.

from setuptools import setup

# Ideally, we should use `pip.req.parse_requirements` to parse the
# `requirements.txt` file (e.g. remove comments), but this function does not
# have a public API, and therefore no backwards compatibility contract.
#
# As a compromise, we read `requirements.txt` as a plain text file, and require
# that file does not have any advanced syntax.
#
# See also:
# http://stackoverflow.com/questions/14399534/
# https://github.com/pypa/pip/issues/2422
with open("requirements.txt", 'r') as f:
    install_requires = f.read().splitlines()

setup(
    name = "xy_python_utils",
    version = "0.1.dev",
    url = "https://github.com/yxiong/xy_python_utils",
    author = "Ying Xiong",
    author_email = "yxiong@seas.harvard.edu",
    description = "Python utilities by Ying Xiong.",
    packages = ["xy_python_utils",],
    install_requires = install_requires
)
