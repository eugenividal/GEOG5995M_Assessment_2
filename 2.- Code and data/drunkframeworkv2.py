# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:51:04 2018

@author: ts16evt
"""
import random

# Define a drunk class.
class Drunk():
    def __init__(self, environment, densitymap, drunks, name):
        self.drunks = drunks
        self.environment = environment
        self.densitymap = densitymap
        self.x = 158 # reference line 24
        self.y = 148
        self.name = name

# Method to move.
# % is a torus boundary in order to keep the drunks inside the defined environment.
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

# Method to eat. 
    def steps(self):
        self.densitymap[self.y][self.x] += 1      

#def go_home(self)