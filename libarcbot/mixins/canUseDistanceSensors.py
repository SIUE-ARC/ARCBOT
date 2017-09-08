#!/usr/bin/env python3
from libarcbot.hardware.infrared import Infrared
from libarcbot.hardware.ultrasonic import UltraSonic

class CanUseDistanceSensors(object):
    """docstring for CanUseDistanceSensors."""
    __ir = None
    __ur = None

    def __init__(self):
        super(CanUseDistanceSensors, self).__init__()
        self.__ir = Infrared()
        self.__us = UltraSonic()

    """
    Get IR 0 value

    :returns: Float value in meters
    """

    def get_ir_zero(self, angle):
        return self.__ir.get_value(0)

    """
    Get IR 1 value

    :returns: Float value in meters
    """

    def get_ir_one(self, angle):
        return self.__ir.get_value(1)

    """
    Get IR 3 value

    :returns: Float value in meters
    """

    def get_ir_three(self, angle):
        return self.__ir.get_value(3)

    """
    Get Ultra Sonic 0 value

    :returns: Float value in meters
    """

    def get_ultra_sonic_zero(self, angle):
        return self.__us.get_value(0)

    """
    Get Ultra Sonic 1 value

    :returns: Float value in meters
    """

    def get_ultra_sonic_one(self, angle):
        return self.__us.get_value(1)

    """
    Get Ultra Sonic 3 value

    :returns: Float value in meters
    """

    def get_ultra_sonic_three(self, angle):
        return self.__us.get_value(3)
