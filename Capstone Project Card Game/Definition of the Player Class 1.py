# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:34:23 2024

@author: hp
"""

class Player(object):
    """ a player """
    def __init__(self, name):
        """ sets the name and an empty hand """
        self.hand = []
        self.name = name
    def get_name(self):
        """ Returns the name of the player """
        return self.name
        
        