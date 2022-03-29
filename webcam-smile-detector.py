# Simple Face Detector that draws a rectangle around any face in a webcam stream

from ast import While
from threading import Timer
import time
from tkinter import font
from weakref import finalize
import cv2
import PySimpleGUI as sg

webcam = cv2.VideoCapture(0)
trained_face_data = cv2.CascadeClassifier(
    "data/haarcascade_frontalface_default.xml")

trained_smile_data = cv2.CascadeClassifier(
    "data/haarcascade_smile.xml")

while True:
    successful_frame_read, frame = webcam.read()

    #grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(
        frame)
    # smile_coordinates = trained_smile_data.detectMultiScale(
    #    frame, scaleFactor=1.7, minNeighbors=10)

    for coordinates in face_coordinates:

        (x, y, w, h) = coordinates
        # draw rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

        # face coordinates
        the_face = frame[y: y + h, x: x + w]

        # convert face to grayscale
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        # find smiles in face frame only
        smiles = trained_smile_data.detectMultiScale(
            face_grayscale, scaleFactor=1.7, minNeighbors=20)

        for (x_, y_, w_, h_) in smiles:
            # draw rectangle around smile
            cv2.rectangle(the_face, (x_, y_),
                          (x_ + w_, y_ + h_), (255, 0, 0), 4)

        if len(smiles) > 0:
            cv2.putText(frame, 'smiling', (x, y+h+40), fontScale=3,
                        fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))

    cv2.imshow('Clever', frame)
    key = cv2.waitKey(1)

    if(key == 81 or key == 113):
        break

webcam.release()
print("Completed")
