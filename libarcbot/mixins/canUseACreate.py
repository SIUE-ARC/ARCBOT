#!/usr/bin/env python3
from libarcbot.create.create import Create


class CanUseACreate(object):
    """docstring for CanUseACreate."""
    __create = None

    def __init__(self, arg):
        super(CanUseACreate, self).__init__()
        self.__create = Create()

    """
    Drive the Create given a speed and radius

    :param speed: The speed in M/s
    :param radius: Radius of the turn from to the center of the create in M
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """

    def create_drive(self, speed, radius):
        if -255 < speed < 255 and -2 * math.pi < radius < 2 * math.pi:
            self.__create.drive(speed, radius)
        else:
            raise TypeError

    """
    Drive the Create motors directly

    :param lspeed: speed of the left motor
    :param rspeed: speed of the right motor
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """

    def create_drive_direct(self, lspeed, rspeed):
        if -255 < lspeed < 255 and -255 < rspeed < 255:
            self.__create.drive_direct(lspeed, rspeed)
        else:
            raise TypeError

    """
    Stop the Create

    :returns: void
    """

    def create_stop(self):
        self.__create.drive_direct(0, 0)

    """
    Put the Create in Safe Mode

    :returns: void
    """

    def create_safe(self):
        self.__create.set_mode("safe")

    """
    Put the Create in Full Mode

    :returns: void
    """

    def create_full(self):
        self.__create.set_mode("full")

    """
    Put the Create in the Spot Demo

    :returns: void
    """

    def create_spot(self):
        self.__create.set_demo("spot")

    """
    Put the Create in the Cover Demo

    :returns: void
    """

    def create_cover(self):
        self.__create.set_demo("cover")

    """
    Put the Create in the Cover Dock Demo

    :returns: void
    """

    def create_cover_dock(self):
        self.__create.set_demo("dock")

    """
    Get the Create Left Bumper Sensor Value

    :returns: Integer value for the Bumper
    """

    def get_create_left_bumper(self):
        return self.__create.get_bumper("left")

    """
    Get the Create Right Bumper Sensor Value

    :returns: Integer value for the Bumper
    """

    def get_create_right_bumper(self):
        return self.__create.get_bumper("right")

    """
    Get the Create Left Drop Sensor Value

    :returns: Integer value for the Sensor
    """

    def get_create_left_drop(self):
        return self.__create.get_drop("left")

    """
    Get the Create Center Drop Sensor Value

    :returns: Integer value for the Sensor
    """

    def get_create_center_drop(self):
        return self.__create.get_drop("center")

    """
    Get the Create Right Drop Sensor Value

    :returns: Integer value for the Sensor
    """

    def get_create_right_drop(self):
        return self.__create.get_drop("right")

    """
    Get the Create Left Wheel Drop Sensor Value

    :returns: Integer value for the Sensor
    """

    def get_create_left_wheel_drop(self):
        return self.__create.get_wheel_drop("left")

    """
    Get the Create Right Wheel Drop Sensor Value

    :returns: Integer value for the Sensor
    """

    def get_create_right_wheel_drop(self):
        return self.__create.get_wheel_drop("right")

    """
    Get the Create Center Wheel Drop Sensor Value

    :returns: Integer value for the Sensor
    """

    def get_create_center_wheel_drop(self):
        return self.__create.get_wheel_drop("center")

    """
    Get the Create Left Cliff Sensor Value

    :returns: Integer value for the Sensor
    """

    def get_create_left_cliff(self):
        return self.__create.get_clif("left")

    """
    Get the Create Front Left Cliff Sensor Value

    :returns: Integer value for the Sensor
    """

    def get_create_front_left_cliff(self):
        return self.__create.get_cliff("front left")

    """
    Get the Create Right Cliff Sensor Value

    :returns: Integer value for the Sensor
    """

    def get_create_right_cliff(self):
        return self.__create.get_cliff("right")

    """
    Get the Create Front Right Cliff Sensor Value

    :returns: Integer value for the Sensor
    """

    def get_create_front_right_cliff(self):
        return self.__create.get_cliff("front right")
    """
    Tell the create to continue at its current velocity until it has reached
    the specified distance

    :param distance: Distance for the create to travel in Meters
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """

    def create_wait_distance(self, distance):
        if -255 < distance < 255:
            self.__create.wait_distance(distance)
        else:
            raise TypeError

    """
    Tell the create to continue at its current speed until it has reached the
    specified angle

    :param angle: Angle to turn to in Degrees
    :returns: void
    :raises TypeError: TypeError when invalid input is provided
    """

    def create_wait_angle(self, angle):
        if -255 < angle < 255:
            self.__create.wait_angle(angle)
        else:
            raise TypeError

    """
    Tell the create to continue at its current velocity until a wheel is dropped

    :returns: void
    """

    def create_wait_wheel_drop(self):
        self.__create.wait_event("Wheel Drop")

    """
    Tell the create to continue at its current velocity until the front wheel is
    dropped

    :returns: void
    """

    def create_wait_front_wheel_drop(self):
        self.__create.wait_event("Front Wheel Drop")

    """
    Tell the create to continue at its current velocity until the left wheel is
    dropped

    :returns: void
    """

    def create_wait_left_wheel_drop(self):
        self.__create.wait_event("Left Wheel Drop")

    """
    Tell the create to continue at its current velocity until the right wheel is
    dropped

    :returns: void
    """

    def create_wait_right_wheel_drop(self):
        self.__create.wait_event("Right Wheel Drop")

    """
    Tell the create to continue at its current velocity until the Bump sensor is
    tripped

    :returns: void
    """

    def create_wait_bump(self):
        self.__create.wait_event("Bump")

    """
    Tell the create to continue at its current velocity until the left bumper is
    triggered

    :returns: void
    """

    def create_wait_left_bumper(self):
        self.__create.wait_event("Left Bump")

    """
    Tell the create to continue at its current velocity until the right bumper is
    triggered

    :returns: void
    """

    def create_wait_right_bumper(self):
        self.__create.wait_event("Right Bump")

    """
    Tell the create to continue at its current velocity until the create hits a
    virtual wall

    :returns: void
    """

    def create_wait_virtual_wall(self):
        self.__create.wait_event("Virtual Wall")

    """
    Tell the create to continue at its current velocity until the cliff sensor
    is triggered

    :returns: void
    """

    def create_wait_cliff(self):
        self.__create.wait_event("Cliff")

    """
    Tell the create to continue at its current velocity until the left cliff is
    triggered

    :returns: void
    """

    def create_wait_left_cliff(self):
        self.__create.wait_event("Left Cliff")

    """
    Tell the create to continue at its current velocity until the front left
    cliff is triggered

    :returns: void
    """

    def create_wait_front_left_cliff(self):
        self.__create.wait_event("Front Left Cliff")

    """
    Tell the create to continue at its current velocity until the front right
    cliff is triggered

    :returns: void
    """

    def create_wait_front_right_cliff(self):
        self.__create.wait_event("Front Right Cliff")

    """
    Tell the create to continue at its current velocity until the right cliff
    is triggered

    :returns: void
    """

    def create_wait_right_cliff(self):
        self.__create.wait_event("Right Cliff")

    """
    Tell the create to continue at its current velocity until the create is in
    a home base

    :returns: void
    """

    def create_wait_home_base(self):
        self.__create.wait_event("Home Base")

    """
    Tell the create to continue at its current velocity until the advance Button
    is pressed

    :returns: void
    """

    def create_wait_advance_button(self):
        self.__create.wait_event("Advance Button")

    """
    Tell the create to continue at its current velocity until the Play Button is
    pressed

    :returns: void
    """

    def create_wait_play_button(self):
        self.__create.wait_event("Play Button")

    """
    Tell the create to continue at its current velocity until Digital Input 0 is
    high

    :returns: void
    """

    def create_wait_digital_zero(self):
        self.__create.wait_event("Digital Input 0")

    """
    Tell the create to continue at its current velocity until Digital Input 1 is
    high

    :returns: void
    """

    def create_wait_digital_one(self):
        self.__create.wait_event("Digital Input 1")

    """
    Tell the create to continue at its current velocity until Digital Input 2 is
    high

    :returns: void
    """

    def create_wait_digital_two(self):
        self.__create.wait_event("Digital Input 2")

    """
    Tell the create to continue at its current velocity until Digital Input 3 is
    high

    :returns: void
    """

    def create_wait_digital_three(self):
        self.__create.wait_event("Digital Input 3")

    """
    Tell the create to continue at its current velocity until the create is in
    passive mode

    :returns: void
    """

    def create_wait_passive_mode(self):
        self.__create.wait_event("Passive")

    # TODO: LEDS
    # TODO: Songs
