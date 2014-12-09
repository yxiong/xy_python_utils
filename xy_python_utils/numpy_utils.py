#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Mar 13, 2014.

"""Some extended utility functions for 'numpy' module."""

import numpy as np

def null(A, tol = 1e-12):
    """Return the null space of matrix or vector 'A', such that
        dot(A, null(A)) == eps(M, N)
    Each column 'r' of null(A) is a unit vector, and ||dot(A, r)|| < tol.
    """
    A = np.atleast_2d(A)
    _, s, vt = np.linalg.svd(A)
    nnz = (s >= tol).sum()
    return vt[nnz:].T
