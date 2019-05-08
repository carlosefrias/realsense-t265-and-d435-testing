import pyrealsense2 as rs
import numpy as np 
import cv2
import os

pipe = rs.pipeline()

cfg = rs.config()
cfg.enable_stream(rs.stream.fisheye, 1)
cfg.enable_stream(rs.stream.fisheye, 2)

pipe.start(cfg)

left_path = './data/left'
right_path = './data/right'
file_format = 'jpg'
# Check if folder path exists before creating folders
if not os.path.exists(left_path) or not os.path.isdir(left_path):
    os.makedirs(left_path)
if not os.path.exists(right_path) or not os.path.isdir(right_path):
    os.makedirs(right_path)

cv2.namedWindow('left', cv2.WINDOW_NORMAL)
cv2.namedWindow('right', cv2.WINDOW_NORMAL)

try:
    for i in range(200):
        frames = pipe.wait_for_frames()

        left = frames.get_fisheye_frame(1)
        left_data = np.asanyarray(left.get_data())

        right = frames.get_fisheye_frame(2)
        right_data = np.asanyarray(right.get_data())

        cv2.imshow('left', left_data)
        cv2.imshow('right', right_data)

        cv2.imwrite(f'{left_path}/{str(i)}.{file_format}', left_data)
        cv2.imwrite(f'{right_path}/{str(i)}.{file_format}', right_data)

        cv2.waitKey(500)
except:
    print("Unable to capture frames.")
finally:
    pipe.stop()