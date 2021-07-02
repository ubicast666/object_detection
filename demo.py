"""
编写一个带有图像化界面的程序，点击预测可以利用摄像头进行拍摄，然后自动预测出结果，呈现出来
"""

import cv2

capture = cv2.VideoCapture(0)
if capture.isOpened():
    ret, frame = capture.read()
    cv2.imshow("frame", frame)
    cv2.waitKey(0)
    cv2.destroyWindow("frame")
else:
    print("摄像头无法打开")
