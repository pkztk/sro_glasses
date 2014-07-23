#!/usr/bin/python2

import sys, os, glob


def fileLength(file):
    return sum(1 for line in file)


def getCoordinates(file):

    at_coords = {}

    for i in range(fileLength(file)):

        if i > 1 and file[i].split()[0] == "0":
            at_coords[int(file[i].split()[0]) + 10000 + i - 1] = map(float, file[i].split()[1:4])

        elif file[i].split()[0] == "1":
            at_coords[int(file[i].split()[0]) + 10000 - i] = map(float, file[i].split()[1:4])

    return at_coords

def getNeighbors(file):
    
    at_neighbors = []

    


for file in glob.glob('*.xyz'):
    f = open(file, "r").readlines()
    print getCoordinates(f)

