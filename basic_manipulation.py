import cv2
import matplotlib.pyplot as plt

cb = cv2.imread("images\checkerboard_18x18.png")

cb_copy = cb.copy()

cb_copy[1,2] = 100
cb_copy[2,2] = 100


cv2.imshow("Pixel manipulation",cb_copy)
cv2.waitKey(0)