#!/usr/bin/python2

import glob, methods

def one(file):
    print "Each atom nearest neighbors - density {:.2f} g/cm^3:".format(methods.density(file))
    neighbors_call = methods.getNeighbors(file)
    for key, value in neighbors_call.items():
        print "{}\t{}".format(key, value)


def two(file):
    print "Coordination numbers - density {:.2f} g/cm^3:".format(methods.density(file))
    coord_number_Si = methods.coordNumber_Si(file)
    for key, value in coord_number_Si[0].items():
        print "{}-fold: {}%".format(key, 100 * float(value) / coord_number_Si[1])


def three(file):
    print "Bond lengths - density {:.2f} g/cm^3:".format(methods.density(file))
    bonds = methods.bondLength(file)
    print "Si-O: {:.2f}\nO-O: {:.2f}\nSi-Si: {:.2f}".format(*bonds)


def four(file):
    print "Angles - density {:.2f} g/cm^3:".format(methods.density(file))
    angle = methods.angles(file)
    print "O-Si-O: {:.2f}\nSi-O-Si: {:.2f}".format(*angle)


def five(file):
    print "Ring distribution in % (total quantity in brackets) - density {:.2f} g/cm^3:".format(methods.density(file))
    rings = methods.rings(file)
    for key, value in rings[0].items():
        print "{}-membered: {:.2f}% ({})".format(key, 100 * float(value) / rings[1], value)


print """
         What would you like to get?

         1) neighbors list                          4) O-Si-O and Si-O-Si angles
         2) coordination number of Si atoms         5) ring statistics 
         3) bond lengths      
                                                             """   

answer  = input("Select an option: ")
print 

        
options = {1 : one, 2 : two, 3 : three, 4 : four, 5 : five}


if answer == 2:
    methods.removeFiles("coord*")
elif answer == 3:
    methods.removeFiles("bond*")
elif answer == 4:
    methods.removeFiles("angles*")
elif answer == 5:
    methods.removeFiles("*_membered")


for file in sorted(glob.glob('*.xyz')):
    f = open(file, "r").readlines()
    options[answer](f)
    print

