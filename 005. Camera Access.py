import cv2
import sys

s = 0
if len(sys.argv) > 1:
  s = sys.argv[1]

source = cv2.VideoCapture(s)

while cv2.waitKey(1) != 27:
  hasFrame, frame = source.read()
  if not hasFrame:
    break
  cv2.imshow("Video", frame)

source.release()
cv2.destroyWindow("Video")