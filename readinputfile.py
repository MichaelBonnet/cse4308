# Reads the input file
def readInputFiles(fName):
    filedata = open(fName, 'r')
    datastructure = {}
    for i in filedata:
        i = i.lstrip()
        i = i.rstrip()
        i = i.rstrip('\n')
        i = i.rstrip('\r')
        if i != 'END OF INPUT':
            citydist = i.split(' ')
            citydist[2] = float(citydist[2])

            if citydist[0] in datastructure:  # handle city 1 --> city 2
                datastructure[citydist[0]].append([citydist[1], citydist[2]])
            else:
                datastructure[citydist[0]] = [[citydist[1], citydist[2]]]
            if citydist[1] in datastructure:  # handle city 2 --> city 1
                datastructure[citydist[1]].append([citydist[0], citydist[2]])
            else:
                datastructure[citydist[1]] = [[citydist[0], citydist[2]]]
        else:
            return datastructure