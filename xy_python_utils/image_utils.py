#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Dec 11, 2014.

import math
import scipy
import numpy as np

def imresize(img, size):
    """Resize the input image.

    Parameters
    ----------
    img: the input image to be resized.

    size: a scalar for `scale` or a 2-tuple for `(num_rows, num_cols)`.
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
            num_rows = num_cols * img.shape[2] / img.shape[1]
        if num_cols < 0:
            num_cols = num_rows * img.shape[1] / img.shape[2]
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
    icons: a list of icons to be put together for mosaic.
        Currently we require all icons to be multi-channel images of the same
        size.

    icon_shape: the shape of icons in the output mosaic.
        If not specified, use the shape of first image in `icons`.

    border_size: the size of border.

    border_color: the color of border, black if not specified.

    empty_color: the color for empty cells, black if not specified.

    mosaic_shape: the shape of output mosaic.
        If not specified, try to make a square mosaic according to number of
        icons.

    mosaic_dtype: the `dtype` of output mosaic.

    Returns
    -------
    mosaic_image: the created mosaic image.

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
