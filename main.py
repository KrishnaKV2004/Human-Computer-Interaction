import cv2
import numpy as np
import time

from config import *
from utils.gesture_utils import get_distance
from utils.cursor_control import left_click, right_click, drag_start, drag_end
from utils.screen_utils import move_cursor
from tracking.hand_tracker import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

detector = HandDetector()
prev_x, prev_y = 0, 0
smooth_x, smooth_y = 0, 0
left_clicked = right_clicked = drag_started = False
last_click_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    detector.find_hands(frame)
    points = detector.get_landmark_points(frame.shape)

    if points:
        index_finger, thumb, middle_finger = points[8], points[4], points[12]

        # Screen Mapping
        x = np.interp(index_finger[0], [0, CAM_WIDTH], [0, SCREEN_WIDTH])
        y = np.interp(index_finger[1], [0, CAM_HEIGHT], [0, SCREEN_HEIGHT])

        # Smoothing
        smooth_x = prev_x + (x - prev_x) / SMOOTHING_FACTOR
        smooth_y = prev_y + (y - prev_y) / SMOOTHING_FACTOR
        prev_x, prev_y = smooth_x, smooth_y

        move_cursor(smooth_x, smooth_y)

        # Gesture Detection
        dist_thumb_index = get_distance(thumb, index_finger)
        dist_index_middle = get_distance(index_finger, middle_finger)
        current_time = time.time()

        # Left Click
        if dist_thumb_index < 25 and current_time - last_click_time > CLICK_DELAY:
            if not left_clicked:
                left_click()
                left_clicked = True
                last_click_time = current_time
        else:
            left_clicked = False

        # Right Click
        if dist_index_middle < 25 and current_time - last_click_time > CLICK_DELAY:
            if not right_clicked:
                right_click()
                right_clicked = True
                last_click_time = current_time
        else:
            right_clicked = False

        # Dragging
        if dist_thumb_index < 25:
            if not drag_started:
                drag_start()
                drag_started = True
        else:
            if drag_started:
                drag_end()
                drag_started = False

        detector.draw_hands(frame)

    cv2.imshow("Smooth Hand Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()