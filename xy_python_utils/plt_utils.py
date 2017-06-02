#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Jun 02, 2017.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.cbook import iterable

def histb(x, bins=None, **kargs):
    """Same as `plt.hist`, but clips out-of-boundary data points to the terminal bins."""
    if iterable(bins):
        x = np.copy(x)
        x_min = (bins[0] + bins[1]) / 2
        x_max = (bins[-2] + bins[-1]) / 2
        x[x < x_min] = x_min
        x[x > x_max] = x_max
    plt.hist(x, bins, **kargs)
