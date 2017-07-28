import os

import cv2
import numpy as np


class Camera(object):
    """Camera Interface"""
    __testing = False
    __camera_id = 0
    __capture = None
    __low_rgb = None
    __high_rgb = None

    def __init__(self, camera_id, testing=False):
        super(Camera, self).__init__()
        self.__testing = testing
        self.__camera_id = camera_id if camera_id > -1 else 0

        try:
            self.open_camera()
        except Exception:
            raise

    def set_rgb_ranges(self, low_rgb, high_rgb):
        if isinstance(low_rgb, list):
            self.__low_rgb = np.array(low_rgb)
        elif isinstance(low_rgb, np.ndarray):
            self.__low_rgb = low_rgb
        else:
            self.__low_rgb = np.array([0, 0, 0])

        if isinstance(high_rgb, list):
            self.__high_rgb = np.array(low_rgb)
        elif isinstance(high_rgb, np.ndarray):
            self.__high_rgb = high_rgb
        else:
            self.__high_rgb = np.array([255, 255, 255])

    # noinspection PyArgumentList
    def open_camera(self):
        if not self.__testing:
            self.__capture = cv2.VideoCapture(self.__camera_id)
            if not self.__capture.isOpened():
                raise RuntimeError("Unable to open the camera")
        else:
            cwd = os.getcwd()
            image_url = "/home/ryan/build/ARCBOT/libarcbot/camera/testimages/testimage.jpg"
            try:
                self.__capture = cv2.imread(image_url)
            except Exception:
                raise

    def get_frame(self):
        if self.__testing:
            return self.__capture
        flag, frame = self.__capture.read()
        if flag:
            return frame
        else:
            raise IOError("Unable to read from the Camera")

    def find_contours_threshold(self, thresh_val=0, max_val=10, thresh_type=0):
        # given a frame
        frame = self.get_frame()
        # convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # then threshold the image with the given threshold value, max value, and threshold type
        _, threshold = cv2.threshold(gray_frame, thresh_val, max_val, thresh_type)
        # TODO Use cv2.RETR_EXTERNAL and cv2.CHAIN_APPROX_TC89_L1 like KIPR?
        # then find the contours
        image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return image, contours, hierarchy

    def find_contours_in_range(self, low_rgb, high_rgb, thresh_type=0):
        # given low and high HSV values
        # and a frame
        frame = self.get_frame()
        # run in range given low and high HSV values and the frame
        mask = cv2.inRange(frame, low_rgb, high_rgb)
        # then erode the mask
        mask = cv2.erode(mask, None)  # TODO Need iteration count?
        # then dilate the image
        mask = cv2.dilate(mask, None)  # TODO Need iteration count?
        # then find the contours
        # TODO Use cv2.RETR_EXTERNAL and cv2.CHAIN_APPROX_TC89_L1 like KIPR?
        image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return image, contours, hierarchy

    def get_objects(self):
        # given the low and high RGB ranges
        if self.__low_rgb is None or self.__high_rgb is None:
            return []
        # given the image, contours, and hierarchy
        image, contours, hierarchy = self.find_contours_in_range(self.__low_rgb, self.__high_rgb)
        # get the moment for each contour
        moments = []
        for contour in contours:
            moments.append(cv2.moments(contour, False))

        # get the camera_object for each contour
        camera_objects = []
        for i, contour in enumerate(contours):
            x, y, w, h = cv2.boundingRect(contour)

            # get the moment for this contour
            moment = moments[i]
            # get the confidence in the Rectangle
            confidence = moment['m00'] / (w * h)
            # get the XY point of the moment
            point = (moment['m10'] / moment['m00'], moment['m01'] / moment['m00'])
            # setup the rectangle
            rectangle = (x, y, w, h)
            # now get the camera_object
            camera_object = (point, rectangle, confidence)
            # save the camera_object
            camera_objects.append(camera_object)
        return camera_objects
