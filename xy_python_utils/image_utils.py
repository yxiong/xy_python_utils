#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Dec 11, 2014.

"""Some utility functions to handle images."""

import math
import numpy as np
import PIL
import scipy

def imresize(img, size):
    """Resize the input image.

    Parameters
    ----------
    img: ndarray
        The input image to be resized.

    size: a scalar for `scale` or a 2-tuple for `(num_rows, num_cols)`
        One of the `num_rows` or `num_cols` can be -1, which will be inferred
        such that the output image has the same aspect ratio as the input.

    Returns
    -------
    The resized image.

    """
    if hasattr(size, "__len__"):
        num_rows, num_cols = size
        assert (num_rows > 0) or (num_cols > 0)
        if num_rows < 0:
            num_rows = num_cols * img.shape[0] / img.shape[1]
        if num_cols < 0:
            num_cols = num_rows * img.shape[1] / img.shape[0]
    else:
        num_rows = int(round(img.shape[0] * size))
        num_cols = int(round(img.shape[1] * size))
    try:
        import cv2
        return cv2.resize(img, (num_cols, num_rows))
    except ImportError:
        import scipy.ndimage
        zoom = [float(num_rows)/img.shape[0], float(num_cols)/img.shape[1]]
        if len(img.shape) == 3:
            zoom.append(1.0)
        return scipy.ndimage.interpolation.zoom(img, zoom)

def create_icon_mosaic(icons, icon_shape=None,
                       border_size=1, border_color=None, empty_color=None,
                       mosaic_shape=None, mosaic_dtype=np.float):
    """Create a mosaic of image icons.

    Parameters
    ----------
    icons: a list of `ndarray`s
        A list of icons to be put together for mosaic. Currently we require all
        icons to be multi-channel images of the same size.

    icon_shape: 2-tuple, optional
        The shape of icons in the output mosaic as `(num_rows, num_cols)`. If
        not specified, use the shape of first image in `icons`.

    border_size: int, optional
        The size of border.

    border_color: 3-tuple, optional
        The color of border, black if not specified.

    empty_color: 3-tuple, optional
        The color for empty cells, black if not specified.

    mosaic_shape: 2-tuple, optional
        The shape of output mosaic as `(num_icons_per_row,
        num_icons_per_col)`. If not specified, try to make a square mosaic
        according to number of icons.

    mosaic_dtype: dtype
        The data type of output mosaic.

    Returns
    -------
    The created mosaic image.

    """
    # Set default parameters.
    num_icons = len(icons)
    assert num_icons > 0
    if icon_shape is None:
        icon_shape = icons[0].shape
    assert len(icon_shape) == 3
    num_channels = icon_shape[2]
    if border_color is None:
        border_color = np.zeros(num_channels)
    if empty_color is None:
        empty_color = np.zeros(num_channels)
    if mosaic_shape is None:
        num_cols = int(math.ceil(math.sqrt(num_icons)))
        num_rows = int(math.ceil(float(num_icons) / num_cols))
        mosaic_shape = (num_rows, num_cols)
    mosaic_image_shape = (
        mosaic_shape[0] * icon_shape[0] + (mosaic_shape[0]-1) * border_size,
        mosaic_shape[1] * icon_shape[1] + (mosaic_shape[1]-1) * border_size,
        icon_shape[2])
    # Create mosaic image and fill with border color.
    mosaic_image = np.empty(mosaic_image_shape, dtype=mosaic_dtype)
    for c in xrange(mosaic_image.shape[2]):
        mosaic_image[:,:,c] = border_color[c]
    # Fill in the input icons.
    for idx in xrange(num_icons):
        i = idx / mosaic_shape[1]
        j = idx % mosaic_shape[1]
        iStart = i * (icon_shape[0] + border_size)
        jStart = j * (icon_shape[1] + border_size)
        mosaic_image[iStart:iStart+icon_shape[0],
                     jStart:jStart+icon_shape[1],:] = icons[idx]
    # Fill the empty icons with empty colors.
    for idx in xrange(num_icons, mosaic_shape[0]*mosaic_shape[1]):
        i = idx / mosaic_shape[1]
        j = idx % mosaic_shape[1]
        iStart = i * (icon_shape[0] + border_size)
        jStart = j * (icon_shape[1] + border_size)
        for c in xrange(mosaic_image.shape[2]):
            mosaic_image[iStart:iStart+icon_shape[0],
                         jStart:jStart+icon_shape[1],c] = empty_color[c]
    return mosaic_image

def image_size_from_file(filename):
    """Read the image size from a file.

    This function only loads but the image header (rather than the whole
    rasterized data) in order to determine its dimension.

    Parameters
    ----------
    filename: string
        The input image file.

    Returns
    -------
    The 2-tuple for image size `(num_rows, num_cols)`.

    """
    with PIL.Image.open(filename) as img:
        width, height = img.size
    return height, width
