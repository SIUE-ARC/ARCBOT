#!/usr/bin/env python3
from libarcbot.utils.commandconstants import __CommandConstants


class Create(object):
    """docstring for Create."""
    __serial_manager = None
    __command_constants = __CommandConstants()
    __MAX_VELOCITY_IN_METERS_PER_SECOND = 0.5
    __STRAIGHT_RADIUS = 0x7FFF
    __CLOCKWISE_RADIUS = 0xFFFF
    __COUNTER_CLOCKWISE_RADIUS = 0x0001
    __MAX_RADIUS_IN_METERS = 2

    def __init__(self, serial_manager):
        super(Create, self).__init__()
        self.__serial_manager = serial_manager

    def drive(self, speed, radius):
        # given a command
        command = self.__command_constants.CREATE_DRIVE_COMMAND
        # and the speed with radius
        command = command + str(speed) + str(radius)
        # send the command and get the response
        return self.__serial_manager.send_command(command + self.__command_constants.SERIAL_TERMINATOR)

    def drive_direct(self, lspeed, rspeed):
        # given a command
        command = self.__command_constants.CREATE_DRIVE_DIRECT_COMMAND
        # and the left and right wheel speeds
        command = command + str(lspeed) + str(rspeed)
        # send the command and get the response
        return self.__serial_manager.send_command(command + self.__command_constants.SERIAL_TERMINATOR)

    def set_moode(self, mode):
        if mode == "safe":
            command = self.__command_constants.CREATE_SAFE_MODE_COMMAND
        elif mode == "full":
            command = self.__command_constants.CREATE_FULL_MODE_COMMAND
        else:
            raise TypeError
        self.__serial_manager.send_command(command + self.__command_constants.SERIAL_TERMINATOR)

    def set_demo(self, demo):
        command = self.__command_constants.CREATE_DEMO_MODE_COMMAND
        if demo == "spot":
            command = command + str(self.__command_constants.CREATE_SPOT_COVER_DEMO_MODE)
        elif demo == "cover":
            command = command + str(self.__command_constants.CREATE_COVER_DEMO_MODE)
        elif demo == "dock":
            command = command + str(self.__command_constants.CREATE_COVER_DOCK_DEMO_MODE)
        else:
            raise TypeError
        self.__serial_manager.send_command(command + self.__command_constants.SERIAL_TERMINATOR)
