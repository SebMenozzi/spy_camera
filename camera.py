import time
import datetime
import cv2
import imutils
import numpy as np
from base_camera import BaseCamera

class Camera(BaseCamera):

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(0)

        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            img = imutils.rotate(img, 180)
            img = imutils.resize(img, width=450)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = np.dstack([ img, img, img ])

            timestamp = datetime.datetime.now()
            ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
            cv2.putText(img, ts, (20, img.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (255, 255, 255), 1)

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
