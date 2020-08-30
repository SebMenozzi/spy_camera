import time
import datetime
import cv2
import imutils
from base_camera import BaseCamera
from imutils.video import FileVideoStream

class Camera(BaseCamera):
    @staticmethod
    def frames():
        fvs = FileVideoStream(0).start()

        while fvs.more():
            img = fvs.read()

            # rotate image 180
            img = imutils.rotate(img, 180)
            img = imutils.resize(img, width=450)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            timestamp = datetime.datetime.now()
            ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
            cv2.putText(img, ts, (20, img.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (255, 255, 255), 1)

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
