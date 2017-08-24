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

    def is_valid_velocity(self, velocity):
        return velocity < self.__MAX_VELOCITY_IN_METERS_PER_SECOND and velocity > -self.__MAX_VELOCITY_IN_METERS_PER_SECOND

    def is_valid_radius(self, radius):
        return radius < self.__MAX_RADIUS_IN_METERS and radius > -self.__MAX_RADIUS_IN_METERS

    def drive_straight_at_velocity(self, velocity):
        # given a valid velocity
        if not self.is_valid_velocity(velocity):
            return -1
        # and a command
        command = self.__command_constants.CREATE_DRIVE_COMMAND
        # send the command
        return self.__serial_manager.send_command(command + velocity + self.__STRAIGHT_RADIUS)

    def turn_in_place(self, velocity):
        # given a valid velocity
        if not self.is_valid_velocity(velocity):
            return -1
        # and a command
        command = self.__command_constants.CREATE_DRIVE_COMMAND
        # and a direction
        if velocity < 0:
            direction = self.__COUNTER_CLOCKWISE_RADIUS
        else:
            direction = self.__CLOCKWISE_RADIUS
        # send the command
        return self.__serial_manager.send_command(command + velocity + direction)

    def turn_by_radius_at_velocity(self, velocity, radius):
        # given a valid velocity
        if not self.is_valid_velocity(velocity):
            return -1
        # and a valid radius
        if not self.is_valid_radius(radius):
            return -1
        # and a command
        command = self.__command_constants.CREATE_DRIVE_COMMAND
        # send the command
        return self.__serial_manager.send_command(command + velocity + radius)
