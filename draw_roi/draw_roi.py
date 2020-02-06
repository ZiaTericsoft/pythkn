'''
THIS CODE IS USE TO DRAW RECTANGLE ON FRAMES i.e WE CAN DEFINE ROI
'''

# IMPORT LIBRARIES
import cv2
import numpy as np

# DETECT MOUSE EVENTS AND APPEND COORDINATES TO CIRCLES
def mouse_drawing(event,x,y, flags, params):
  # print(event)
  if event == cv2.EVENT_LBUTTONDOWN:
    # print("left")
    # print(x,y)
    circles.append((x,y))

# READS VIDEO SOURCE
cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouse_drawing)
circles = []

# REDS FRAME AND ALSO DRAW RECTANGLE ON FRAME
'''
PRESS Q TO DELETE
PRESS D TO DELETE ALL CORDINATES
'''
def read_frames(circles):
  while True:
    _, frame = cap.read()
    # print(len(circles))
    if len(circles) %2 ==0:
      for x in range(0,len(circles)):
        if x %2==0:
          a_1 = circles[x]
          b_1 = circles[x+1]
          cv2.rectangle(frame ,a_1, b_1, (0,255,0))

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
      break
    elif key == ord('d'):
      circles = []

  cv2.destroyAllWindows()


read_frames(circles)