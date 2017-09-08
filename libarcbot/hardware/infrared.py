#!/usr/bin/env python3
from libarcbot.serialmanager.serialmanager import SerialManager
from libarcbot.utils.commandconstants import __CommandConstants

class Infrared(object):
    """docstring for Infrared."""
    __serial_manager = None
    __command_constants = None

    def __init__(self):
        super(Infrared, self).__init__()
        self.__serial_manager = SerialManager.get_instance()
        self.__command_constants = __CommandConstants()

    def get_value(self, id):
        # given a command
        command = self.__command_constants.IR_GET_COMMAND
        # and an IR id
        command = command + str(id)
        # send the command, returning the value
        return float(self.__serial_manager.send_command(command + self.__command_constants.SERIAL_TERMINATOR))
