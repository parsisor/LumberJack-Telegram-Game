import cv2
import numpy as np
import mss
import pyautogui
import time
from pynput import keyboard

running = True

def on_press(key):
    global running
    if key == keyboard.Key.space:
        running = False
        return False

listener = keyboard.Listener(on_press=on_press)
listener.start()

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0


def mask(hsv):
    mask1 = cv2.inRange(hsv, (5, 60, 20), (25, 255, 200))
    mask2 = cv2.inRange(hsv, (0, 40, 10), (30, 200, 180))
    return cv2.bitwise_or(mask1, mask2)


def brown_count(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return cv2.countNonZero(mask(hsv))


def roi(frame, x1, y1, x2, y2):
    return frame[y1:y2, x1:x2]

# rectangle cords
area1 = (1525, 351, 1618, 510)
area2 = (1698, 349, 1813, 510)

threshold = 80

cooldown = 0.12  
last = 0

last_side = "right"

# cordination of right and left button
leftcl = (1567, 735)
rightcl = (1771, 732)

with mss.MSS() as sct:

    monitor = sct.monitors[1]

    while running:

        now = time.time()

        frame = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        c1 = brown_count(roi(frame, *area1))
        c2 = brown_count(roi(frame, *area2))

        left_ok = c1 < threshold
        right_ok = c2 < threshold

        if now - last > cooldown:

            if not left_ok and not right_ok:

                if last_side == "left":
                    pyautogui.click(leftcl)
                else:
                    pyautogui.click(rightcl)

                last = now

            elif left_ok and right_ok:

                if last_side == "right":
                    pyautogui.click(leftcl)
                    last_side = "left"
                else:
                    pyautogui.click(rightcl)
                    last_side = "right"

                last = now

            elif left_ok:
                pyautogui.click(leftcl)
                last_side = "left"
                last = now

            elif right_ok:
                pyautogui.click(rightcl)
                last_side = "right"
                last = now

        time.sleep(0.01)

print("Stopped")