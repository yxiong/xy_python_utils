#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Oct 28, 2014.

import math
import matplotlib.pyplot as plt

def impixelinfo(ax=None, image=None):
    """Mimic Matlab's `impixelinfo` function that shows the image pixel
    information as the cursor swipes through the figure.

    Parameters
    ----------
    ax: the axes that tracks cursor movement and prints pixel information.
        We require the `ax.images` list to be non-empty, and if more than one
        images present in that list, we examine the last (newest) one. If not
        specified, default to 'plt.gca()'.

    image: if specified, use this `image`'s pixel instead of `ax.images[-1]`'s.
        The replacement `image` must have the same dimension as `ax.images[-1]`,
        and we will still be using the `extent` of the latter when tracking
        cursor movement.

    Returns
    -------
    None

    """
    # Set default 'ax' to 'plt.gca()'.
    if not ax:
        ax = plt.gca()
    # Examine the number of images in 'ax'.
    if len(ax.images) == 0:
        print "No image in axes to visualize."
        return
    # Set default 'image' if not specified.
    if not image:
        image = ax.images[-1].get_array()
    # Get the 'extent' of current image.
    (left,right,bottom,top) = ax.images[-1].get_extent()

    # Re-define the 'format_coord' function and assign it to 'ax'.
    def format_coord(x, y):
        """Return a string formatting the `x`, `y` coordinates, plus additional
        image pixel information."""
        result_str = "(%.3f, %.3f): " % (x, y)
        # Get the image pixel index.
        i = int(math.floor((y - top) / (bottom - top) * image.shape[0]))
        j = int(math.floor((x - left) / (right - left) * image.shape[1]))
        # Return early if (i,j) is out of boundary.
        if (i < 0) or (i >= image.shape[0]) or (j < 0) or (j >= image.shape[1]):
            return result_str
        # Get the pixel value and add to return string.
        if (len(image.shape) == 3) and (image.shape[2] == 4):
            # 4-channel RGBA image.
            result_str += "(%.3f, %.3f, %.3f, %.3f)" % \
                          (image[i,j,0], image[i,j,1],
                           image[i,j,2], image[i,j,3])
        elif (len(image.shape) == 3) and (image.shape[2] == 3):
            # 3-channel RGB image.
            result_str += "(%.3f, %.3f, %.3f)" % \
                          (image[i,j,0], image[i,j,1], image[i,j,2])
        else:
            # Single-channel grayscale image.
            assert len(image.shape) == 2
            result_str += "%.3f" % image[i,j]
        return result_str
    ax.format_coord = format_coord

def axes_equal_3d(ax=None):
    """Mimic Matlab's `axis equal` command. The matplotlib's command
    `ax.set_aspect("equal")` only works for 2D plots, but not for 3D plots
    (those generated with `projection="3d"`).

    Parameters
    ----------
    ax: the axes whose x,y,z axis to be equalized.
        If not specified, default to `plt.gca()`.

    """
    # Set default 'ax' to 'plt.gca()'.
    if not ax:
        ax = plt.gca()

    # Get the mid-point and range for each dimension.
    def mid_and_range(lim):
        return (lim[0] + lim[1])/2.0, (lim[1] - lim[0])

    x_mid, x_range = mid_and_range(ax.get_xlim())
    y_mid, y_range = mid_and_range(ax.get_ylim())
    z_mid, z_range = mid_and_range(ax.get_zlim())

    # Set the range for each dimension to be 'max_range'.
    max_range = max(x_range, y_range, z_range)
    ax.set_xlim(x_mid - max_range/2.0, x_mid + max_range/2.0)
    ax.set_ylim(y_mid - max_range/2.0, y_mid + max_range/2.0)
    ax.set_zlim(z_mid - max_range/2.0, z_mid + max_range/2.0)

def implay(volume, fps=20, ax=None):
    """Play a sequence of image in `volume` as a video.

    Parameters
    ----------
    volume: the video volume to be played.
        Its size can be either MxNxK (for single-channel image per frame) or
        MxNxCxK (for multi-channel image per frame).

    fps: the frame rate of the video.

    ax: the axes in which the video to be played.
        If not specified, default to `plt.gca()`.

    """
    if not ax:
        ax = plt.gca()
    num_frames = volume.shape[-1]
    for i in xrange(num_frames):
        ax.cla()
        ax.imshow(volume[...,i])
        plt.pause(1. / fps)

def tight_subplot(num_rows, num_cols, plot_index,
                  gap = 0.01, marg_h = 0.01, marg_w = 0.01, fig = None):
    """Add a tight subplot axis to the current (or a given) figure.

    Parameters
    ----------
    num_rows: number of rows.

    num_cols: number of columns.

    plot_index: the index to the subplot.

    gap: the gap between axes, scalar or 2-tuple `(gap_h, gap_w)`.
        Value should be between (0, 1).

    marg_h: the margins in height, scalar or 2-tuple `(lower, upper)`.
        Value should be between (0, 1).

    marg_w: the margins in width, scalar or 2-tuple `(left, right)`.
        Value should be between (0, 1).

    fig: figure to which the new axes to be added to
        Default to `plt.gcf()` if not specified.

    Returns
    -------
    The newly added axes.

    """
    if not hasattr(gap, "__len__"):
        gap = (gap, gap)
    if not hasattr(marg_h, "__len__"):
        marg_h = (marg_h, marg_h)
    if not hasattr(marg_w, "__len__"):
        marg_w = (marg_w, marg_w)
    if not fig:
        fig = plt.gcf()

    m = int(math.ceil(float(plot_index) / num_cols))
    n = plot_index - (m-1) * num_cols

    height = float(1 - marg_h[0] - marg_h[1] - gap[0] * (num_rows-1)) / num_rows
    width = float(1 - marg_w[0] - marg_w[1] - gap[1] * (num_cols-1)) / num_cols

    bottom = marg_h[0] + (height + gap[0]) * (num_rows - m)
    left = marg_w[0] + (width + gap[1]) * (n - 1)
    return fig.add_axes((left, bottom, width, height))

def imshow(ax, img, xlim=None, ylim=None, **kw):
    """Enhance `ax.imshow` with coordinate limits.

    Parameters
    ----------
    ax: the axes in which an image will be drawn.

    img: the 2D image to be drawn.

    xlim, ylim: the horizontal coordinate limits of the image.
        This will set the `extent` parameter of `ax.imshow`, which is relatively
        inconvenient to set directly because of the half-pixel issue.
        Default: (0, `num_cols`-1), (0, `num_rows`-1).

    **kw: other parameters to be passed to `ax.imshow`.
        The `extent` will be ignored if presented.

    Returns
    -------
    None

    """
    if not xlim:
        xlim = (0, img.shape[1]-1)
    if not ylim:
        ylim = (0, img.shape[0]-1)

    xmin, xmax = xlim
    ymin, ymax = ylim
    dx = float(xmax - xmin) / img.shape[1]
    dy = float(ymax - ymin) / img.shape[0]
    # Note the order: (left, right, bottom, top)
    kw["extent"] = (xmin-dx/2.0, xmax+dx/2.0, ymax+dy/2.0, ymin-dy/2.0)

    ax.imshow(img, **kw)

def draw_with_fixed_lims(ax, draw_fcn):
    """Save the `xlim` and `ylim` of `ax` before a drawing action, and restore
    them after the drawing. This is typically useful when one first does an
    `imshow` and then makes some annotation with `plot`, which will change the
    limits if not using this function.

    """
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    draw_fcn(ax)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)