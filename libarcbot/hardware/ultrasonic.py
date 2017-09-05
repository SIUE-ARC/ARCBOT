#!/usr/bin/env python3
from libarcbot.utils.commandconstants import __CommandConstants

class UltraSonic(object):
    """docstring for Infrared."""
    __serial_manager = None
    __command_constants = __CommandConstants()

    def __init__(self, serial_manager):
        super(Infrared, self).__init__()
        self.__serial_manager = serial_manager

    def get_value(self, id):
        # given a command
        command = self.__command_constants.US_GET_COMMAND
        # and an IR id
        command = command + str(id)
        # send the command, returning the value
        return float(self.__serial_manager.send_command(command + self.__command_constants.SERIAL_TERMINATOR))
