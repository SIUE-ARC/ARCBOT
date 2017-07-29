#!/usr/bin/env python3


class Create(object):
    """docstring for Create."""
    self.__serial_manager = None
    self.__byte_order = 'big'

    def __init__(self, serial_manager):
        super(Create, self).__init__()
        self.__serial_manager = serial_manager

    def get_left_bumper(self):
        # given the getter command
        command = "GET LEFT BUMPER COMMAND"
        # and the serial manager
        serial = self.__serial_manager
        # send the command, and get the result
        result = serial.send_command(command)
        # now return it
        return int.from_bytes(result, byteorder=self.__byte_order)

    def get_right_bumper(self):
        # given the getter command
        command = "GET RIGHT BUMPER COMMAND"
        # and the serial manager
        serial = self.__serial_manager
        # send the command, and get the result
        result = serial.send_command(command)
        # now return it
        return int.from_bytes(result, byteorder=self.__byte_order)

    def get_left_drop(self):
        # given the getter command
        command = "GET LEFT DROP COMMAND"
        # and the serial manager
        serial = self.__serial_manager
        # send the command, and get the result
        result = serial.send_command(command)
        # now return it
        return int.from_bytes(result, byteorder=self.__byte_order)

    def get_right_drop(self):
        # given the getter command
        command = "GET RIGHT DROP COMMAND"
        # and the serial manager
        serial = self.__serial_manager
        # send the command, and get the result
        result = serial.send_command(command)
        # now return it
        return int.from_bytes(result, byteorder=self.__byte_order)

    def get_center_drop(self):
        # given the getter command
        command = "GET CENTER DROP COMMAND"
        # and the serial manager
        serial = self.__serial_manager
        # send the command, and get the result
        result = serial.send_command(command)
        # now return it
        return int.from_bytes(result, byteorder=self.__byte_order)
