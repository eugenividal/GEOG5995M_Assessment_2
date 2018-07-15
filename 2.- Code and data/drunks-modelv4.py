# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:48:17 2018
GEOG5995M Programming for Social Science: Core Skills
@author: Eugeni Vidal

"""
# The algorith for the model:
# 1. Set up the environment
# 2. Make the drunks
# 3. Move the drunks
# 4. Draw the density
# 5. Save the density map to a file as text

# First, we import all packages we will need for the code
import csv
import matplotlib.pyplot
import matplotlib.animation
import drunkframeworkv4

# 1. Set up the environment
## Create the list.
environment = []

## Read the raster data.
f = open('drunk.plan.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

## Put drunk.plan file csv into rows
for row in reader:
    rowlist =[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

"""
## Check how the environment looks
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
"""    
## Find the location of the pub
for y, row in enumerate(environment):
    for x, value in enumerate(row):
        if value == 1:
            print(x, y)

#for y in range(len(environment)):
#    print(y)
#    rowlist = []
#    for x in range(len(environment[y])):
#        rowlist.append(0)
#    densitymap.append(rowlist)

# 2. Make the drunks 
## Set up the drunks list.
drunks = []
num_of_drunks = 25; #number drunks range(10, 250, 10)
num_of_iterations = 1000000 #infinite steps could be more exact 

## Animating.
#fig = matplotlib.pyplot.figure(figsize=(5, 5))
#ax = fig.add_axes([0, 0, 1, 1])

## Make and name them.
for i in range(num_of_drunks):
    name = ((1+i)*10)
#   print(name)
    drunks.append(drunkframeworkv4.Drunk(environment, drunks, name))
    
# 3. Move the drunks (from the pub to the house)
for i in range (num_of_drunks):
    drunk = drunks[i]
    for j in range(num_of_iterations):
        if environment [drunk.y][drunk.x] != drunk.name:
            drunks[i].move()
#            drunks[i].steps()

## Test
for drunk in drunks:
    print('next agent')
    print(drunk.name)
    print(environment[drunk.y][drunk.x])

## Check how the envrinment looks
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_drunks):
    matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y)
matplotlib.pyplot.show()

# 4. Draw the density of drunks (passing through each point on a map).

# 5. Save the density map to a file as text.
with open('output.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        csvwriter.writerow(row)
        
with open('drunks.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for drunk in drunks:
        row = [drunk.name, drunk.x, drunk.y]
        csvwriter.writerow(row)