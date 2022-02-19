import cv2

vdo = cv2.VideoCapture("images/race_car.mp4")

# while cv2.waitKey(1) != 27:
#   ret, frame = vdo.read()
#   if not ret:
#     break
#   cv2.imshow("Video", frame)
# cv2.destroyAllWindows()

width = int(vdo.get(3))
height = int(vdo.get(4))

vdo_out = cv2.VideoWriter("images/out_video.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (width, height))

while(vdo.isOpened()):

  ret, frame = vdo.read()

  if ret == True:
    vdo_out.write(frame)
  else:
    break
vdo_out.release()
vdo.release()