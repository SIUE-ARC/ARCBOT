from unittest import TestCase
import numpy as np
import cv2
from libarcbot.camera.camera import Camera

class TestCamera(TestCase):
    camera = Camera(0, True)

    def test_get_frame(self):
        frame = self.camera.get_frame()
        # size of the image is width * height * 3 (where the three is number of values for each pixel)
        self.assertEqual(frame.size, (640*400*3))

    def test_find_contours_threshold(self):
        image, contours, _ = self.camera.find_contours_threshold(1, 10, 0)
        self.assertEqual(len(contours), 243)

        _, contours, _ = self.camera.find_contours_threshold(0, 10, 0)
        self.assertEqual(len(contours), 291)

    def test_find_contours_in_range(self):
        low_rgb = np.array([254, 99, 0])
        high_rgb = np.array([255, 255, 255])
        _, contours, _ = self.camera.find_contours_in_range(low_rgb, high_rgb)
        self.assertEqual(len(contours), 5)

    def test_get_objects(self):
        low_rgb = np.array([254, 99, 0])
        high_rgb = np.array([255, 255, 255])
        self.camera.set_rgb_ranges(low_rgb, high_rgb)
        objects = self.camera.get_objects()
        self.assertEqual(len(objects), 5)
