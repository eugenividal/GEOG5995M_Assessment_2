# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:48:17 2018
GEOG5995M Programming for Social Science: Core Skills
@author: Eugeni Vidal

"""
# The algorithm for the model:
# 1. Set up the environment
# 2. Make the drunks and give them a name
# 3. Move the drunks and draw the density
# 4. Save the density map to a file as text

# First, we import all packages we will need for the model.
import csv
import matplotlib.pyplot
import matplotlib.animation
import drunkframework

# 1. Set up the environment.
## Create the list.
environment = []

## Read the raster data.
f = open('drunk.plan.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

## Put drunk.plan file csv into rows.
for row in reader:
    rowlist =[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

## Check how the environment looks.
"""
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
"""    

# 2. Make the drunks and give them a name.
## Create the list.
drunks = []
## Stablish the number of drunks and iterations.
num_of_drunks = 25; # Number drunks range(10, 250, 10).
num_of_iterations = 1000000 # Infinite steps would have been better, but dind't know how to do it.

## Code to size the plot and animating.
fig = matplotlib.pyplot.figure(figsize=(5, 5))
ax = fig.add_axes([0, 0, 1, 1])

## Make and name the drunks.
for i in range(num_of_drunks):
    name = ((1+i)*10) # because Python starts in 0 we have to add 1 first and then just multiply by 10.
#   print(name) # test names are right
    drunks.append(drunkframework.Drunk(environment, drunks, name))
    
# 3. Move the drunks and draw the density.
for i in range (num_of_drunks):
    drunk = drunks[i]
    for j in range(num_of_iterations):
        if environment [drunk.y][drunk.x] != drunk.name: # move the drunks until they don't find their own home
            drunks[i].move()
            drunks[i].steps()
            
## Plot to check if the model works
matplotlib.pyplot.xlim(0,300)
matplotlib.pyplot.ylim(0,300)

matplotlib.pyplot.imshow(environment)
for i in range(num_of_drunks):
    matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y)

matplotlib.pyplot.show()

# 4. Save the density map to a file as text.
with open('environment.density.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        csvwriter.writerow(row)
        
"""
THE END 
"""