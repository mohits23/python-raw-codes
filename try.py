import cv2
import numpy as np

image = cv2.imread('F:/myImages/MohitWall.png')
image[np.where((image==[255,255,255]).all(axis=2))] = [0,255,255]
cv2.imwrite('F:/myImages/redMS.png', image)
