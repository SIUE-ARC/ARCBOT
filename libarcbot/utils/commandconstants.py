#!/usr/bin/env python3
from libarcbot.utils.constant import constant


class __CommandConstants(object):
    """Create Command Constants"""
    @constant
    def SERIAL_TERMINATOR():
        return "\\r"

    @constant
    def CREATE_MODE_COMMANDS():
        return {
            'safe': 'A',
            'full': 'B'
        }

    @constant
    def CREATE_DEMO_MODE_COMMAND():
        return "C"

    @constant
    def CREATE_DEMO_IDS():
        return {
            'cover': 0,
            'dock': 1,
            'spot': 2,
            'mouse': 3,
            'eight': 4,
            'wimp': 5
        }

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

    @constant
    def CREATE_BUMPER_COMMAND():
        return "P"

    # TODO: Get the actual IDS
    @constant
    def CREATE_BUMPER_IDS:
        return {
            'left': 0,
            'right': 1
        }

    @constant
    def CREATE_DROP_SENSORS_COMMAND():
        return "Q"

    # TODO: Get the actual ids
    @constant
    def CREATE_DROP_SENSOR_IDS():
        return {
            'left': 0,
            'center': 1,
            'right': 2
        }

    @constant
    def CREATE_WHEEL_DROP_COMMAND():
        return "R"

    # TODO: Get the actual ids
    @constant
    def CREATE_WHEEL_IDS():
        return {
            'left': 0,
            'center': 1,
            'right': 2
        }

    @constant
    def CREATE_CLIFF_COMAMND():
        return "S"

    # TODO: Get the actual IDS
    @constant
    def CREATE_CLIFF_IDS():
        return {
            'left': 0,
            'front left': 1
            'right': 2,
            'front right': 3
        }
