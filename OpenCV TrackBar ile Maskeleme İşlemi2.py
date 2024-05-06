# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:39:49 2024

@author: necip
"""

# -*- coding: utf-8 -*-

import cv2
import numpy as np

# Constants
MAX_HUE = 180
MAX_SATURATION = 255
MAX_VALUE = 255

def create_trackbars(window_name):
    cv2.createTrackbar("Lower Hue", window_name, 0, MAX_HUE, lambda x: None)
    cv2.createTrackbar("Lower Saturation", window_name, 0, MAX_SATURATION, lambda x: None)
    cv2.createTrackbar("Lower Value", window_name, 0, MAX_VALUE, lambda x: None)
    cv2.createTrackbar("Upper Hue", window_name, 0, MAX_HUE, lambda x: None)
    cv2.createTrackbar("Upper Saturation", window_name, 0, MAX_SATURATION, lambda x: None)
    cv2.createTrackbar("Upper Value", window_name, 0, MAX_VALUE, lambda x: None)

def set_initial_trackbar_positions(window_name):
    cv2.setTrackbarPos("Upper Hue", window_name, 150)
    cv2.setTrackbarPos("Upper Saturation", window_name, 150)
    cv2.setTrackbarPos("Upper Value", window_name, 150)

def main():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("bar")
    cv2.resizeWindow("bar", 600, 600)
    create_trackbars("bar")
    set_initial_trackbar_positions("bar")

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_hue = cv2.getTrackbarPos("Lower Hue", "bar")
        lower_saturation = cv2.getTrackbarPos("Lower Saturation", "bar")
        lower_value = cv2.getTrackbarPos("Lower Value", "bar")
        upper_hue = cv2.getTrackbarPos("Upper Hue", "bar")
        upper_saturation = cv2.getTrackbarPos("Upper Saturation", "bar")
        upper_value = cv2.getTrackbarPos("Upper Value", "bar")

        lower_color = np.array([lower_hue, lower_saturation, lower_value])
        upper_color = np.array([upper_hue, upper_saturation, upper_value])

        mask = cv2.inRange(frame_hsv, lower_color, upper_color)

        cv2.imshow("Original", frame)
        cv2.imshow("Mask", mask)

        if cv2.waitKey(20) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()