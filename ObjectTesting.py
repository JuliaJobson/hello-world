#!/usr/bin/python3

class Recipe(object):
    """ This is an object made to understand the creation and handling of
    objects in pyhton3 """
    def __init__(self, list, minutes):
        self._ingredient = list
        self._time = minutes

    def display_ingredient(self):
        for i in self._ingredient:
            print(i)

    def catch_ingredient(self):
        return self._ingredient

    def catch_time(self):
        return self._time
