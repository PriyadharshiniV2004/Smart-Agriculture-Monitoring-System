import cv2
import numpy as np

def preprocess_image(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([25, 50, 50])
    upper = np.array([75, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    masked = cv2.bitwise_and(img, img, mask=mask)

    white_bg = np.ones_like(img) * 255
    final = cv2.addWeighted(masked, 1, white_bg, 1, 0)

    return final
