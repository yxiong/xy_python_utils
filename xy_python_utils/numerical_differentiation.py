#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Mar 19, 2014.

import numpy as np

def numerical_jacobian(fcn, x0, dx=1e-6, method=0, return_f0=False):
    """Compute the numerical Jacobian matrix of a given function.

    Parameters
    ----------
    fcn: a function handle that takes an N-vector as input and return an M-vector.
    x0: an input N-vector.
    dx: a scalar for small change in x0.
    method: a integer or string with following options:
      * {0, 'forward'}: compute the Jacobian as (f(x0+dx)-f(x0))/dx.
      * 1, 'central' : compute the Jacobian as (f(x0+dx)-f(x0-dx))/2/dx.
    return_f0: if set to true, also return fcn(x0).

    Returns
    -------
    J: the MxN Jacobian matrix.
    f0: the function value at x0.

    Examples
    --------
    >>> J = numerical_jacobian(fcn, x0, ...)
    >>> (J, f0) = numerical_jacobian(fcn, x0, ..., return_f0=True)
    """
    N = len(x0)
    if method==0 or method=="forward":
        # Forward difference.
        f0 = fcn(x0)
        M = len(f0)
        J = np.zeros((M,N))
        for j in xrange(N):
            xj = x0.copy()
            xj[j] += dx
            fj = fcn(xj)
            J[:,j] = (fj-f0) / dx
        if return_f0:
            return (J, f0)
        else:
            return J
    elif method==1 or method=="central":
        # Central difference.
        for j in xrange(N):
            xj1 = x0.copy()
            xj2 = x0.copy()
            xj1[j] -= dx
            xj2[j] += dx
            fj1 = fcn(xj1)
            fj2 = fcn(xj2)
            if j == 0:
                M = len(fj1)
                J = np.zeros((M,N))
            J[:,j] = (fj2-fj1) / 2 / dx
        if return_f0:
            return (J, fcn(x0))
        else:
            return J
    else:
        assert False, "Unknown method '" + method + "'."
