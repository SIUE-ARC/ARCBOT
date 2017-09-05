#!/usr/bin/env python3

import math
from libarcbot.camera.camera import Camera
from libarcbot.create.create import Create
from libarcbot.utils.constants import Constants
from libarcbot.serialmanager.serialmanager import SerialManager


class ArcBot(object):
    """Arc Bot Library Interface"""
    __camera = None
    __serial = None
    __create = None

    def __init__(self):
        super(ArcBot, self).__init__()
        self.__camera = Camera()
        self.__serial = SerialManager.get_instance()
        self.__create = Create(self.__serial)

    """
    Drive the Create given a speed and radius

    :param speed: The speed in M/s
    :param radius: Radius of the turn from to the center of the create in M
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """
    def create_drive(self, speed, radius):
        if -255 < speed < 255 and -2 * math.pi < radius < 2 * math.pi:
            self.__create.drive(speed, radius)
        else:
            raise TypeError

    """
    Drive the Create motors directly

    :param lspeed: speed of the left motor
    :param rspeed: speed of the right motor
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """
    def create_drive_direct(self, lspeed, rspeed):
        if -255 < lspeed < 255 and -255 < rspeed < 255:
            self.__create.drive_direct(lspeed, rspeed)
        else:
            raise TypeError

    """
    Stop the Create

    :returns: void
    """
    def create_stop(self):
        self.__create.drive_direct(0, 0)

    """
    Put the Create in Safe Mode

    :returns: void
    """
    def create_safe(self):
        self.__create.set_mode("safe")

    """
    Put the Create in Full Mode

    :returns: void
    """
    def create_full(self):
        self.__create.set_mode("full")

    """
    Put the Create in the Spot Demo

    :returns: void
    """
    def create_spot(self):
        self.__create.set_demo("spot")

    """
    Put the Create in the Cover Demo

    :returns: void
    """
    def create_cover(self):
        self.__create.set_demo("cover")

    """
    Put the Create in the Cover Dock Demo

    :returns: void
    """
    def create_cover_dock(self):
        self.__create.set_demo("dock")

    """
    Get the Create Left Bumper Sensor Value

    :returns: Integer value for the Bumper
    """
    def get_create_left_bumper(self):
        return self.__create.get_bumper("left")

    """
    Get the Create Right Bumper Sensor Value

    :returns: Integer value for the Bumper
    """
    def get_create_right_bumper(self):
        return self.__create.get_bumper("right")

    """
    Get the Create Left Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_left_drop(self):
        return self.__create.get_drop("left")

    """
    Get the Create Center Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_center_drop(self):
        return self.__create.get_drop("center")

    """
    Get the Create Right Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_right_drop(self):
        return self.__create.get_drop("right")

    """
    Get the Create Left Wheel Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_left_wheel_drop(self):
        return self.__create.get_wheel_drop("left")

    """
    Get the Create Right Wheel Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_right_wheel_drop(self):
        return self.__create.get_wheel_drop("right")

    """
    Get the Create Center Wheel Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_center_wheel_drop(self):
        return self.__create.get_wheel_drop("center")

    """
    Get the Create Left Cliff Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_left_cliff(self):
        return self.__create.get_clif("left")

    """
    Get the Create Front Left Cliff Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_front_left_cliff(self):
        return self.__create.get_cliff("front left")

    """
    Get the Create Right Cliff Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_right_cliff(self):
        return self.__create.get_cliff("right")

    """
    Get the Create Front Right Cliff Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_front_right_cliff(self):
        return self.__create.get_cliff("front right")
    """
    Tell the create to continue at its current velocity until it has reached
    the specified distance

    :param distance: Distance for the create to travel in Meters
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """
    def create_wait_distance(self, distance):
        if -255 < distance < 255:
            self.__create.wait_distance(distance)
        else:
            raise TypeError

    """
    Tell the create to continue at its current speed until it has reached the
    specified angle

    :param angle: Angle to turn to in Degrees
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """
    def create_wait_angle(self, angle):
        if -255 < angle < 255:
            self.__create.wait_angle(angle)
        else:
            raise TypeError

    """
    Tell the create to continue at its current velocity until a wheel is dropped

    :returns: void
    """
    def create_wait_wheel_drop(self):
        self.__create.wait_event("Wheel Drop")
