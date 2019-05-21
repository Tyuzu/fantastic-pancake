import cv2
import numpy as np
from matplotlib import pyplot as plt
#loading the image
img = cv2.imread('D67KLdAV4AAquR4.jpg',cv2.IMREAD_GRAYSCALE) #read the image
cv2.imshow('image',img) #show the image
cv2.waitKey(0)
cv2.destroyAllWindows()
