#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Mar 13, 2014.

import unittest

from numpy_utils import *
from unittest_utils import *

class NumpyUtilsTest(unittest.TestCase):
    """Unit test for NumpyUtils."""
    def test_null(self):
        np.random.seed(0)
        tol = 1e-12
        A = np.random.randn(3)
        nA = null(A)
        r = np.dot(A, nA)
        check_near(r, np.zeros(2), tol)
        A = np.random.randn(2,5)
        nA = null(A)
        r = np.dot(A, nA)
        check_near(r, np.zeros((2,3)), tol)

if __name__ == "__main__":
    unittest.main()
