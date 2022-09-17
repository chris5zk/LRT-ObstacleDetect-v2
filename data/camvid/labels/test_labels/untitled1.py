# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 15:07:27 2022

@author: chrischris
"""

import cv2

I2 = cv2.imread('L_rs00012_jpg.rf.bc7fcaa61c369eb303d367e2e541bd88.jpg')

I2[:,:,0:2] = 0

cv2.imshow('a',I2)
cv2.waitKey(0)
cv2.destroyAllWindows()