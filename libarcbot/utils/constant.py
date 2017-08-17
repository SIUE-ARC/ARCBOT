#!/usr/bin/env python3

def constant(f):
    """Constant Value function"""
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)
