#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Dec 11, 2015.

import argparse

"""
Usage:
  python sample_argparse.py -h
  python sample_argparse.py --int=5 -s="Some string"
"""

def main():
    parser = argparse.ArgumentParser(description = "A demo for argparse.")
    parser.add_argument("-i", "--int", type=int, help="An integer argument.", default=123)
    parser.add_argument("-s", "--str", help="A string argument.", default="A default string")
    args = parser.parse_args()

    print args

if __name__ == "__main__":
    main()
