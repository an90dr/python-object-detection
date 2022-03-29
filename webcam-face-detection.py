# Simple Face Detector that draws a rectangle around any face in a webcam stream

from ast import While
from threading import Timer
import time
from weakref import finalize
import cv2
import PySimpleGUI as sg

webcam = cv2.VideoCapture(0)
trained_face_data = cv2.CascadeClassifier(
    "data/haarcascade_frontalface_default.xml")

while True:
    successful_frame_read, frame = webcam.read()

    ##grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(frame)

    for coordinates in face_coordinates:
        (x, y, w, h) = coordinates
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 6)

    cv2.imshow('Clever', frame)
    key = cv2.waitKey(1)

    if(key == 81 or key == 113):
        break

webcam.release()
print("Completed")
