# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:51:04 2018
GEOG5995M Programming for Social Science: Core Skills
@author: Eugeni Vidal

"""
import random

# Define a drunk class.
class Drunk():
    def __init__(self, environment, drunks, name):
        self.drunks = drunks
        self.environment = environment
        self.x = 158 
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
        self.environment[self.y][self.x] += 1      

