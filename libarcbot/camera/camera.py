import os

import cv2


class Camera(object):
    """Camera Interface"""
    __testing = False
    __camera_id = 0
    __capture = None

    def __init__(self, camera_id, testing=False):
        super(Camera, self).__init__()
        self.__testing = testing
        self.__camera_id = camera_id if camera_id > -1 else 0
        try:
            self.opencamera()
        except Exception:
            raise

    # noinspection PyArgumentList
    def opencamera(self):
        if not self.__testing:
            self.__capture = cv2.VideoCapture(self.__camera_id)
            if not self.__capture.isOpened():
                raise RuntimeError("Unable to open the camera")
        else:
            cwd = os.getcwd()
            image_url = cwd + "/testimages/testimage.png"
            try:
                self.__capture = cv2.imread(image_url)
            except Exception:
                raise

    def getframe(self):
        if self.__testing:
            return self.__capture
        flag, frame = self.__capture.read()
        if flag:
            return frame
        else:
            raise IOError("Unable to read from the Camera")

    def findcountours(self, thresh_val, max_val, thresh_type=0):
        frame = self.getframe()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray_frame, thresh_val, max_val, thresh_type)
        image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return image, contours, hierarchy
