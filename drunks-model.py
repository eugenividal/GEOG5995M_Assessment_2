#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 19:56:36 2018

@author: Eugeni Vidal
"""
import matplotlib.pyplot
import matplotlib.animation 
import csv
import drunkframework

#1.Pull in the data file and finds out the pub point and the home points

# Set up environment list (before the drunks list).
environment = []
# Read enviroment data.
f = open('drunk.plan.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist =[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

#3.Models the drunks leaving their pub and reaching their homes, 
#and stores how many drunks pass through each point on the map.
# Set up drunks list.
num_of_drunks = 25; #number drunks range(10, 250, 10)
num_of_iterations = 1000
#num_of_iterations = 100 instead of itetactions from the bpub to home
drunks = []

# Make the drunks.
for i in range(num_of_drunks):
    drunks.append(drunkframework.Drunk(environment, drunks))
    
# Move the drunks. we should move them from the pub to the house
for j in range (num_of_iterations): 
    for i in range(num_of_drunks):
        drunks[i].move()
        drunks[i].path()

#for i in range(num_of_drunks):
#    print("steps" + " " +str(drunks[i].store))
#2.Draws the pub and homes on the screen.

matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_drunks):
    matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y)
matplotlib.pyplot.show()

#4.Draws the density of drunks passing through each point on a map.

#5.Saves the density map to a file as text.
