# Simple Face Detector that draws a rectangle around a face in an imported image

from weakref import finalize
import cv2
import PySimpleGUI as sg


def findFaces(window, img):
    image_elem = window["myImage"]
    trained_face_data = cv2.CascadeClassifier(
        "data/haarcascade_frontalface_default.xml")

    face_coordinates = trained_face_data.detectMultiScale(img)
    for coordinates in face_coordinates:
        (x, y, w, h) = coordinates
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 6)

    imS = cv2.resize(img, (500, 300))
    imgbytes = cv2.imencode('.png', imS)[1].tobytes()
    image_elem.update(data=imgbytes)


def resetImage(window, img):
    image_elem = window["myImage"]
    imgbytes = cv2.imencode('.png', imS)[1].tobytes()
    image_elem.update(data=imgbytes)

# trained_face_data = cv2.CascadeClassifier("data/haarcascade_eye.xml")


img = cv2.imread("img/facesAI2.webp")
# img = cv2.imread("img/AM.JPG")

# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imS = cv2.resize(img, (500, 300))

layout = [[sg.Image(filename='', key='myImage')],
          [sg.Button('Find Face'), sg.Button('Reset')]]

window = sg.Window(title="Hello World", layout=layout,
                   margins=(2, 2), finalize=True)


image_elem = window["myImage"]

imgbytes = cv2.imencode('.png', imS)[1].tobytes()

image_elem.update(data=imgbytes)


while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'Find Face':
        findFaces(window, img)
    elif event == 'Reset':
        resetImage(window, img)

window.Close()


print("Completed")
