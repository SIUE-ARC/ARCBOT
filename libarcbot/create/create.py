#!/usr/bin/env python3
from libarcbot.utils.commandconstants import __CommandConstants

class Create(object):
    """docstring for Create."""
    __serial_manager = None
    __byte_order = 'big'
    __command_constants = __CommandConstants()

    def __init__(self, serial_manager):
        super(Create, self).__init__()
        self.__serial_manager = serial_manager
