#!/usr/bin/env python3
from libarcbot.utils.constant import constant

class __CommandConstants(object):
    """Create Command Constants"""
    @constant
    def SERIAL_TERMINATOR():
        return "\\r"

    @constant
    def CREATE_SAFE_MODE_COMMAND():
        return "A"

    @constant
    def CREATE_FULL_MODE_COMMAND():
        return "B"

    @constant
    def CREATE_DEMO_MODE_COMMAND():
        return "C"

    @constant
    def CREATE_COVER_DEMO_MODE():
        return 0

    @constant
    def CREATE_COVER_DOCK_DEMO_MODE():
        return 1

    @constant
    def CREATE_SPOT_COVER_DEMO_MODE():
        return 2

    @constant
    def CREATE_MOUSE_DEMO_MODE():
        return 3

    @constant
    def CREATE_DRIVE_FIGURE_EIGHT_DEMO_MODE():
        return 4

    @constant
    def CREATE_WIMP_DEMO_MODE():
        return 5

    @constant
    def CREATE_HOME_DEMO_MODE():
        return 6

    @constant
    def CREATE_DRIVE_COMMAND():
        return "D"

    @constant
    def CREATE_DRIVE_DIRECT_COMMAND():
        return "E"

    @constant
    def CREATE_LEDS_COMMAND():
        return "F"

    @constant
    def CREATE_SONG_COMMAND():
        return "G"

    @constant
    def CREATE_PLAY_SONG_COMMAND():
        return "H"

    @constant
    def WAIT_TIME_COMMAND():
        return "I"

    @constant
    def WAIT_DISTANCE_COMMAND():
        return "J"

    @constant
    def WAIT_ANGLE_COMMAND():
        return "K"

    @constant
    def WAIT_EVENT_COMMAND():
        return "L"

    @constant
    def CREATE_ANGLE_COMMAND():
        return "M"

    @constant
    def CREATE_BATTERY_TEMP():
        return "N"

    @constant
    def CREATE_BATTERY_VOLTS():
        return "O"
