import time
import datetime
import cv2
import imutils

class Camera(object):
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        time.sleep(1)

    def __del__(self):
        self.cam.release()

    def get_frame(self):
        success, img = self.cam.read()

        img = imutils.rotate(frame, 180)

        timestamp = datetime.datetime.now()
        ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
        cv2.putText(img, ts, (20, img.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
            0.6, (0, 0, 255), 1)

        ret, jpeg = cv2.imencode('.jpg', img)

        return jpeg.tostring()
