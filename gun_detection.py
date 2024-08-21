import numpy as np
import cv2
import imutils
import datetime
import pygame

pygame.mixer.init()

# Load the pre-trained gun detection cascade classifier
gun_cascade = cv2.CascadeClassifier('cascade.xml')

# Initialize video capture from the default camera (0)
camera = cv2.VideoCapture(0)

firstFrame = None
alarm_on = False

while True:
    ret, frame = camera.read()
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
    gun_exist = False
    for (x, y, w, h) in gun:
        gun_exist = True
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if gun_exist:
        cv2.putText(frame, "Gun Detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 0, 255), 2)
        if not alarm_on:
            pygame.mixer.music.load('alarm.wav')  # Ensure this file exists
            pygame.mixer.music.play(-1)
            alarm_on = True
    else:
        if alarm_on:
            pygame.mixer.music.stop()
            alarm_on = False

    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 0), 1)

    cv2.imshow("Security Feed", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

if gun_exist:
    print("Guns detected")
else:
    print("No guns detected")

camera.release()
cv2.destroyAllWindows()
