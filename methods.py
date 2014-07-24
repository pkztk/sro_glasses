import os

def fileLength(file):
    return sum(1 for line in file)


def reformatFile(file):
    for i in range(fileLength(file)):
        if i > 1 and file[i].split()[0] == "0":
            open("tmp", "a").write("{} {}\n".format(10000 + i - 1, ' '.join(file[i].split()[1:4])))
        elif file[i].split()[0] == "1":
            open("tmp", "a").write("{} {}\n".format(10000 - i, ' '.join(file[i].split()[1:4])))


def distance(a, b, L):
    dummy = 0
    for i in range(3):
        u = a[i] - b[i]
        if u > L/2:
            u -= L
        elif u < -L/2:
            u += L
        dummy += u*u
    return dummy ** 0.5


def getCoordinates(file):
    at_coords = {}
    reformatFile(file)
    for line in open("tmp", "r").readlines():
        at_coords[int(line.split()[0])] = map(float, line.split()[1:4])
    return at_coords


def getNeighbors(file):
    at_neighbors = {}
    L = float(file[1].split()[1])
    coords = getCoordinates(file)
    os.system("voro++ -p -c \"%i %n \" -{0} {0} -{0} {0} -{0} {0} tmp".format(L / 2))
    fp = open("tmp.vol", 'r').readlines()
    for line in fp:
        central = line.split()[0]
        at_neighbors[int(central)] = []
        for atom in line.split()[1:]:
            if distance(coords.get(int(central)), coords.get(int(atom)), L) < 2.0:
                at_neighbors[int(central)].append(int(atom))
    return at_neighbors


def coordNumber_Si(file):
    coord_num = {}
    neighbors = getNeighbors(file)
    for key in neighbors.keys():
        if key > 10000:
            coord_num[len(neighbors[key])] = coord_num.get(len(neighbors[key]), 0) + 1
    return coord_num


