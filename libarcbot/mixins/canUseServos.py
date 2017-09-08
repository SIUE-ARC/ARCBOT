#!/usr/bin/env python3
from libarcbot.hardware.servo import Servo


class CanUseServos(object):
    """docstring for CanUseServos."""
    __servo = None

    def __init__(self):
        super(CanUseServos, self).__init__()
        self.__servo = Servo()

    """
    Move servo 0 to the specified angle

    :param angle: Angle the servo should be move to in degrees
    :param zero: None or Custom value for the Servo Zero
    :param gain: None or Custom value for the Servo Gain
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """

    def set_servo_zero_angle(self, angle, zero=None, gain=None):
        if -360 < angle < 360:
            self.__servo.set_angle(0, angle, zero, gain)
        else:
            raise TypeError

    """
    Move servo 1 to the specified angle

    :param angle: Angle the servo should be move to in degrees
    :param zero: None or Custom value for the Servo Zero
    :param gain: None or Custom value for the Servo Gain
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """

    def set_servo_one_angle(self, angle, zero=None, gain=None):
        if -360 < angle < 360:
            self.__servo.set_angle(1, angle, zero, gain)
        else:
            raise TypeError

    """
    Toggle Servo 0 disable

    :returns: void
    """

    def toggle_servo_zero_disable(self):
        self.__servo.toggle_disable(0)

    """
    Toggle Servo 1 disable

    :returns: void
    """

    def toggle_servo_one_disable(self):
        self.__servo.toggle_disable(1)
