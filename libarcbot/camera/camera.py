import numpy as np
import cv2
import os

class Camera(object):
    """Camera Interface"""
    def __init__(self, camera_id, testing = False):
        super(Camera, self).__init__()
        self.__testing = testing
        print(self.__testing)
        self.__camera_id = camera_id if camera_id > -1 else 0
        try:
            self.openCamera()
        except Exception as e:
            raise

    def openCamera(self):
        if self.__testing == False:
            self.__capture = cv2.VideoCapture(self.__camera_id)
            if self.__capture.isOpened() == False:
                raise RuntimeError("Unable to open the camera")
        else:
            cwd = os.getcwd()
            image_url = cwd + "/testimages/testimage.png"
            try:
                self.__capture = cv2.imread(image_url)
            except Exception as e:
                raise

    def getFrame(self):
        if self.__testing == True:
            return self.__capture
        flag, frame = self.__capture.read()
        if flag == True:
            return frame
        else:
            raise IOError("Unable to read from the Camera")
