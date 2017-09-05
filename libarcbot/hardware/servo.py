#!/usr/bin/env python3
import math
from libarcbot.utils.commandconstants import __CommandConstants


class servo(object):
    """Servo class"""
    __serial_manager = None
    __command_constants = __CommandConstants()

    def __init__(self, serial_manager):
        super(servo, self).__init__()
        self.__serial_manager = serial_manager

    def __convert_degrees_to_ms(self, angle, zero=None, gain=None):
        zero = if zero:
            zero else self.__command_constants.SERVO_ZERO
        gain = if gain:
            gain else self.__command_constants.SERVO_GAIN
        return int(0.5 + zero + gain * angle)

    def set_angle(self, servo, angle, zero=None, gain=None):
        # given a command
        command = self.__command_constants.SET_SERVO_COMMAND
        # and the microseconds for the given angle
        ms = self.__convert_degrees_to_ms(angle, zero, gain)
        # build the full command
        command = command + str(servo) + str(ms)
        # send the command
        self.__serial_manager.send_command(
            command + self.__command_constants.SERIAL_TERMINATOR)
