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
    def CREATE_EVENT_IDS():
        return {
            "Wheel Drop": 1,
            "Front Wheel Drop": 2,
            "Left Wheel Drop": 3,
            "Right Wheel Drop": 4,
            "Bump": 5,
            "Left Bump": 6,
            "Right Bump": 7,
            "Virtual Wall": 8,
            "Wall": 9,
            "Cliff": 10,
            "Left Cliff": 11,
            "Front Left Cliff": 12,
            "Front Right Cliff": 13,
            "Right Cliff": 14,
            "Home Base": 15,
            "Advance Button": 16,
            "Play Button": 17,
            "Digial Input 0": 18,
            "Digital Input 1": 19,
            "Digital Input 2": 20,
            "Digtial Input 3": 21,
            "Passive": 22
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
    def CREATE_BUMPER_IDS():
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
    def SERVO_ZERO():
        return 1000

    @constant
    def SERVO_GAIN():
        return 5.555

    @constant
    def CREATE_CLIFF_COMAMND():
        return "S"

    # TODO: Get the actual IDS
    @constant
    def CREATE_CLIFF_IDS():
        return {
            'left': 0,
            'front left': 1,
            'right': 2,
            'front right': 3
        }

    @constant
    def IR_GET_COMMAND():
        return "T"

    @constant
    def US_GET_COMMAND():
        return "U"
