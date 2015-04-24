#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Dec 09, 2014.

from setuptools import setup

install_requires = [
    "matplotlib",
    "numpy",
    "numpydoc",
    "pillow",
    "scipy",
    "setuptools",
    "sphinx==1.2.3",
]

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
