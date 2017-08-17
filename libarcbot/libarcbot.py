#!/usr/bin/env python3

from libarcbot.camera.camera import Camera
from libarcbot.serialmanager.serialmanager import SerialManager


class ArcBot(object):
    """Arc Bot Library Interface"""
    __camera = None
    __serial = None

    def __init__(self):
        super(ArcBot, self).__init__()
        self.__camera = Camera()
        self.__serial = SerialManager.get_instance()
