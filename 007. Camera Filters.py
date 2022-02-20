import cv2
import numpy as np

webcam = cv2.VideoCapture(0)

PREVIEW = 0
BLUR = 1
CORNER = 2
CANNY = 3

feature_params = dict(maxCorners = 500, qualityLevel = 0.2, minDistance = 15, blockSize = 9)

imageFilter = PREVIEW
alive = True

winName = "Camera Filters"
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
result = None

while(alive):
  hasFrame, frame = webcam.read()
  if not hasFrame:
    break

  frame = cv2.flip(frame, 1)

  if imageFilter == PREVIEW:
    result = frame
  elif imageFilter == BLUR:
    result = cv2.blur(frame, (13, 13))
  elif imageFilter == CANNY:
    result = cv2.Canny(frame, 145, 150)
  elif imageFilter == CORNER:
    result = frame
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
    if corners is not None:
      for x, y in np.int32(corners).reshape(-1, 2):
        cv2.circle(result, (x, y), 10, (0, 0, 255), 2)

  cv2.imshow(winName, result)

  key = cv2.waitKey(1)
  if key == ord('Q') or key == ord('q') or key == 27:
    alive = False
  elif key == ord('C') or key == ord('c'):
    imageFilter = CANNY
  elif key == ord('B') or key == ord('b'):
    imageFilter = BLUR
  elif key == ord('F') or key == ord('f'):
    imageFilter = CORNER

webcam.release()
cv2.destroyWindow(winName)