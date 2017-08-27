#!/usr/bin/env python3

from libarcbot.camera.camera import Camera
from libarcbot.serialmanager.serialmanager import SerialManager


class ArcBot(object):
    """Arc Bot Library Interface"""
    __camera = None
    __serial = None

    def __init__(self):
        super(ArcBot, self).__init__()
        self.__camera = Camera()
        self.__serial = SerialManager.get_instance()

    """
    Drive the Create given a speed and radius

    :param speed: The speed in M/s
    :param radius: Radius of the turn from to the center of the create in M
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """
    def create_drive(self, speed, radius):
        pass

    """
    Drive the Create motors directly

    :param lspeed: speed of the left motor
    :param rspeed: speed of the right motor
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """
    def create_drive_direct(self, lspeed, rspeed):
        pass

    """
    Stop the Create

    :returns: void
    """
    def create_stop(self):
        pass

    """
    Put the Create in Safe Mode

    :returns: void
    """
    def create_safe(self):
        pass

    """
    Put the Create in Full Mode

    :returns: void
    """
    def create_full(self):
        pass

    """
    Put the Create in Safe Mode

    :returns: void
    """
    def create_safe(self):
        pass

    """
    Put the Create in the Spot Demo

    :returns: void
    """
    def create_spot(self):
        pass

    """
    Put the Create in the Cover Demo

    :returns: void
    """
    def create_cover(self):
        pass

    """
    Put the Create in the Cover Dock Demo

    :returns: void
    """
    def create_cover_dock(self):
        pass

    """
    Get the Create Left Bumper Sensor Value

    :returns: Integer value for the Bumper
    """
    def get_create_left_bumper(self):
        pass

    """
    Get the Create Right Bumper Sensor Value

    :returns: Integer value for the Bumper
    """
    def get_create_right_bumper(self):
        pass

    """
    Get the Create Left Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_left_drop(self):
        pass

    """
    Get the Create Center Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_center_drop(self):
        pass

    """
    Get the Create Right Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_right_drop(self):
        pass

    """
    Get the Create Left Wheel Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_left_wheel_drop(self):
        pass

    """
    Get the Create Right Wheel Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_right_wheel_drop(self):
        pass

    """
    Get the Create Center Wheel Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_center_wheel_drop(self):
        pass

    """
    Get the Create Left Cliff Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_left_cliff(self):
        pass

    """
    Get the Create Front Left Cliff Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_front_left_cliff(self):
        pass

    """
    Get the Create Right Cliff Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_right_cliff(self):
        pass

    """
    Get the Create Front Right Cliff Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_right_cliff_drop(self):
        pass

    """
    Get the Create Left Drop Sensor Value

    :returns: Integer value for the Sensor
    """
    def get_create_left_drop(self):
        pass
