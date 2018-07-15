# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:48:17 2018

@author: ts16evt
"""

# First, we import all packages we will need for the code
 
import random
import csv
import matplotlib.pyplot
import matplotlib.animation
import drunkframework

# Set up the environment
## Create the list.
environment = []

## Read the raster data.
f = open('drunk.plan.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist =[]
    for value in row:
        rowlist.append(value)
        if value == 1:
            print('PUB')
    environment.append(rowlist)
f.close()

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
num_of_iterations = 1000
#num_of_iterations = 100 instead of itetactions from the bpub to home

# Animating.
fig = matplotlib.pyplot.figure(figsize=(5, 5))
ax = fig.add_axes([0, 0, 1, 1])

# Make the drunks.
for i in range(num_of_drunks):
    drunks.append(drunkframework.Drunk(environment, drunks))
    
# Move the drunks. we should move them from the pub to the house
for j in range (num_of_iterations): 
      random.shuffle(drunks) # Shuffle the list of agests each iteration before they do their stuff. 
      for i in range(num_of_drunks):
           drunks[i].move()
           drunks[i].steps()

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
