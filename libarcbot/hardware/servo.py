#!/usr/bin/env python3
import math
from libarcbot.serialmanager.serialmanager import SerialManager
from libarcbot.utils.commandconstants import CommandConstants


class Servo(object):
    """Servo class"""
    __serial_manager = None
    __command_constants = None

    def __init__(self):
        super(servo, self).__init__()
        self.__serial_manager = SerialManager.get_instance()
        self.__command_constants = CommandConstants()

    def __convert_degrees_to_ms(self, angle, zero=None, gain=None):
        zero = zero if zero is not None else self.__command_constants.SERVO_ZERO
        gain = gain if gain is not None else self.__command_constants.SERVO_GAIN
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
            command)

    def toggle_disable(self, servo):
        # given a command
        command = self.__command_constants.TOGGLE_SERVO_DISABLE_COMMAND
        # and the servo to toggle
        command = command + str(servo)
        # send the command
        self.__serial_manager.send_command(
            command)
