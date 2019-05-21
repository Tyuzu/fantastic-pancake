import cv2
import numpy as np

# Take each frame
frame = cv2.imread('iu.jpg')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(frame,frame, mask= mask)

laplacian = cv2.Laplacian(frame,cv2.CV_64F)
sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

cv2.imshow('Original',frame)
cv2.imshow('Mask',mask)
cv2.imshow('laplacian',laplacian)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)

cv2.imshow('Original',frame)
edges = cv2.Canny(frame,100,200)
cv2.imshow('Edges',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
