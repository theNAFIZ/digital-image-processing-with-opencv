import cv2

# import image as colored, gray and default
cola_color = cv2.imread("images\coca-cola-logo.png", 1)
cola_gray = cv2.imread("images\coca-cola-logo.png", 0)
cola_uncng = cv2.imread("images\coca-cola-logo.png", -1)

cv2.imshow("Color", cola_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Gray", cola_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Unchanged", cola_uncng)
cv2.waitKey(0)
cv2.destroyAllWindows()

