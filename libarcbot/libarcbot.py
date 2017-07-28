#!/usr/bin/env python3

from libarcbot.camera.camera import Camera


class ArcBot(object):
    """Arc Bot Library Interface"""
    __camera = None

    def __init__(self):
        super(ArcBot, self).__init__()
        self.__camera = Camera(0)
