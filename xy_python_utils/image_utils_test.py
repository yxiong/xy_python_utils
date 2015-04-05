#!/usr/bin/env python
#
# Author: Ying Xiong.
# Created: Jan 07, 2015.

import unittest

from scipy.misc import imread

from image_utils import *
from unittest_utils import check_near

class ImageUtilsTest(unittest.TestCase):
    def test_imresize(self):
        img = imread("test_data/images/testorig.jpg")
        img2 = imresize(img, 0.5)
        self.assertEqual(img2.shape[0], round(img.shape[0]*0.5))
        self.assertEqual(img2.shape[1], round(img.shape[1]*0.5))
        self.assertEqual(img2.shape[2], img.shape[2])

    def test_create_icon_mosaic(self):
        tol = 1e-6
        icon = imread("test_data/images/testorig.png")
        mosaic = create_icon_mosaic([icon] * 6)
        mosaic_ref = imread("test_data/images/testorig-mosaic.png")
        check_near(mosaic, mosaic_ref, tol)

if __name__ == "__main__":
    unittest.main()
