# Simple Face Detector that draws a rectangle around a face in an imported image

from ast import While
from threading import Timer
import time
from weakref import finalize
import cv2
import PySimpleGUI as sg


#img = cv2.imread("img/facesAI2.webp")
# img = cv2.imread("img/AM.JPG")
webcam = cv2.VideoCapture(0)

# while True:
successful_frame_read, frame = webcam.read()
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imS = cv2.resize(frame, (500, 300))

layout = [[sg.Image(filename='', key='myImage')],
          [sg.Button('Find Face'), sg.Button('Reset')]]

window = sg.Window(title="Hello World", layout=layout,
                   margins=(2, 2), finalize=True).Finalize()

image_elem = window["myImage"]

imgbytes = cv2.imencode('.png', imS)[1].tobytes()

image_elem.update(data=imgbytes)

window.read()


while True:
    # hello()
    try:
        successful_frame_read, frame = webcam.read()

        imS = cv2.resize(frame, (500, 300))

        ##image_elem = window["myImage"]

        imgbytes = cv2.imencode('.png', imS)[1].tobytes()

        image_elem.update(data=imgbytes)

        # window.Timeout
        # window.read()
        # press('a')
        # time.sleep(5)
    except NameError:
        print(NameError)
        window.close()
    # window.read()
    # window.clic
    # after 30 seconds, "hello, world" will be printed
    # cv2.waitKey(10)


"""while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'Find Face':
        findFaces(window, img)
    elif event == 'Reset':
        resetImage(window, img)
"""

window.Close()


print("Completed")
