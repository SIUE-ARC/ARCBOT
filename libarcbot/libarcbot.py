#!/usr/bin/env python3

import math
from libarcbot.mixins.canUseACreate import CanUseACreate
from libarcbot.mixins.canUseDistanceSensors import CanUseDistanceSensors
from libarcbot.mixins.canUseServos import CanUseServos
from libarcbot.camera.camera import Camera
from libarcbot.serialmanager.serialmanager import SerialManager


class ArcBot(CanUseACreate, CanUseDistanceSensors, CanUseServos):
    """Arc Bot Library Interface"""
    __camera = None
    __serial = None


    def __init__(self):
        super(ArcBot, self).__init__()
        self.__camera = Camera()
        self.__serial = SerialManager.get_instance()

    def get_serial_manager():
        return self.__serial
