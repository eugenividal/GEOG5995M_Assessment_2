# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:48:17 2018

@author: ts16evt
"""

# First, we import all packages we will need for the code

#import sys
#sys.path.append('C:/Users/ts16evt/OneDrive - University of Leeds/MSc DAS/GEOG5995M PSS/Assessments/Assessment 2/GEOG5995M_Independent_project/2.- Code and data/')

import csv
import matplotlib.pyplot
import matplotlib.animation
import drunkframeworkv3

# Set up the environment
## Create the list.
environment = []
#densitymap = []

## Read the raster data.
f = open('drunk.plan.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# Find the pub
for y, row in enumerate(reader):
    rowlist =[]
    for x, value in enumerate(row):
        rowlist.append(value)
        if value == 1:
            print(x, y)
    environment.append(rowlist)
f.close()

#for y in range(len(environment)):
#    print(y)
#    rowlist = []
#    for x in range(len(environment[y])):
#        rowlist.append(0)
#    densitymap.append(rowlist)

"""
# Check how the envrinment looks
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
"""

# Model the drunks leaving their pub and reaching their homes, 
#and stores how many drunks pass through each point on the map.
# Set up drunks list.
drunks = []
num_of_drunks = 25; #number drunks range(10, 250, 10)
num_of_iterations = 1000000
#num_of_iterations = 100 instead of itetactions from the bpub to home

# Animating.
#fig = matplotlib.pyplot.figure(figsize=(5, 5))
#ax = fig.add_axes([0, 0, 1, 1])

# Make the drunks.
for i in range(num_of_drunks):
    name = ((1+i)*10)
#    print(name)
#    print(drunks)
#    print(environment[5][5])
    drunks.append(drunkframeworkv3.Drunk(environment, drunks, name))
    
# Move the drunks. we should move them from the pub to the house
for i in range (num_of_drunks):
    drunk = drunks[i]
    for j in range(num_of_iterations):
        if environment [drunk.y][drunk.x] != drunk.name:
            drunks[i].move()
#            drunks[i].steps()

# Test

for drunk in drunks:
    print('next agent')
    print(drunk.name)
    print(environment[drunk.y][drunk.x])

# Check how the envrinment looks
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_drunks):
    matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y)
matplotlib.pyplot.show()


with open('output.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        csvwriter.writerow(row)
        
with open('drunks.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for drunk in drunks:
        row = [drunk.name, drunk.x, drunk.y]
        csvwriter.writerow(row)


## Saves the density map to a file as text.
a = []
for i in range(100):
    a.append("All work and no play makes Jack a dull boy ");
f = open("drunks.density.txt", 'w')
for line in a:
	f.write(line)
f.close()

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
