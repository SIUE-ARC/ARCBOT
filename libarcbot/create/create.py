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

    """
    Set Mode - Change which mode the Create is in

    :param mode: The name of the mode to switch to
    :returns: void
    :raises TypeError: raised when an unknown mode is provided
    """

    def set_mode(self, mode):
        # given a dictionary of modes
        ids = self.__command_constants.CREATE_MODE_COMMANDS
        # if the given mode is not in the list of modes, raise an exception
        if mode not in ids:
            raise TypeError
        # get the command to send
        command = ids[mode]
        # and send the command
        self.__serial_manager.send_command(
            command + self.__command_constants.SERIAL_TERMINATOR)

    """
    Set Demo - Runs a specific demo on the create

    :param demo: The demo name to run
    :returns: void
    :raises TypeError: When a demo name is not recognized
    """

    def set_demo(self, demo):
        # given a command
        command = self.__command_constants.CREATE_DEMO_MODE_COMMAND
        # and a list of ids
        ids = self.__command_constants.CREATE_DEMO_IDS
        # if the given demo is not in the list of demos, raise an error
        if demo not in ids:
            raise TypeError
        # add the appropriate ID to the command
        command = command + str(ids[demo])
        # and send the command
        self.__serial_manager.send_command(
            command + self.__command_constants.SERIAL_TERMINATOR)

    """
    Get Bumper - Returns the current create bumper value

    :param bumper: The bumper value to retreive
    :returns: Integer bumper value
    :raises TypeError: When an unsupported bumper is asked for
    """

    def get_bumper(self, bumper):
        # given a command
        command = self.__command_constants.CREATE_BUMPER_COMMAND
        # and the bumper ids
        ids = self.__command_constants.CREATE_BUMPER_IDS
        # if ids does not contain the bumper asked for, throw an exception
        if bumper not in ids:
            raise TypeError
        # add the appropriate ID to the command
        command = command + str(ids[bumper])
        # and send the command, returning the response
        return self.__serial_manager.send_command(command + self.__command_constants.SERIAL_TERMINATOR)

    """
    Get Drop - Returns the value of a given drop sensor

    :param sensor: name of the drop sensor value to return
    :returns: value of the given drop sensor
    :raises TypeError: raised when an unknown sensor name is provided
    """

    def get_drop(self, sensor):
        # given a command
        command = self.__command_constants.CREATE_DROP_SENSORS_COMMAND
        # and the dictionary of sensor ids
        ids = self.__command_constants.CREATE_DROP_SENSOR_IDS
        # if the sensor name is not in the list of ids, raise an exception
        if sensor not in ids:
            raise TypeError
        # append the appropriate sensor id to the command
        command = command + str(ids[sensor])
        # and send the command, returning the value
        return self.__serial_manager.send_command(command + self.__command_constants.SERIAL_TERMINATOR)

    """
    Get Wheel Drop - Returns whether the given wheel is 'dropped'

    :param wheel: the name of the wheel value to return
    :returns: value of the given drop sensor
    :raises TypeError: raised when an invalid wheel name is provided
    """

    def get_wheel_drop(self, wheel):
        # given a command
        command = self.__command_constants.CREATE_WHEEL_DROP_COMMAND
        # and a list of wheel ids
        ids = self.__command_constants.CREATE_WHEEL_IDS
        # if the wheel name is not in the dictionary of ids, raise an exception
        if wheel not in ids:
            raise TypeError
        # append the appropriate wheel id to the command
        command = command + str(ids[wheel])
        # send the command, returning the value
        return self.__serial_manager.send_command(command + self.__command_constants.SERIAL_TERMINATOR)

    """
    Get Clif - Return whether the given cliff sensor is True

    :param cliff: the name of the cliff value to return
    :returns: value of the given cliff sensor
    :raises TypeError: raised when an invalid cliff name is provided
    """

    def get_cliff(self, cliff):
        # given a command
        command = self.__command_constants.CREATE_CLIFF_COMMAND
        # and a list of cliff ids
        ids = self.__command_constants.CREATE_CLIFF_IDS
        # if the cliff name is not in the dictionary of ids, raise an exception
        if cliff not in ids:
            raise TypeError
        # append the appropriate cliff id to the command
        command = command + str(ids[cliff])
        # send the command, returning the value
        return self.__serial_manager.send_command(command + self.__command_constants.SERIAL_TERMINATOR)
