# Read input file
def readInput(fname):
    filedata = open(fname, 'r')
    mapping = {}

    for route in filedata:
        route = route.lstrip()
        route = route.rstrip()
        if route != 'END OF INPUT':
            citydist = route.split(' ')
            citydist[2] = float(citydist[2])

            if citydist[0] in mapping:  # handle city 1 --> city 2
                mapping[citydist[0]].append([citydist[1], citydist[2]])
            else:
                mapping[citydist[0]] = [[citydist[1], citydist[2]]]

            if citydist[1] in mapping:  # handle city 2 --> city 1
                mapping[citydist[1]].append([citydist[0], citydist[2]])
            else:
                mapping[citydist[1]] = [[citydist[0], citydist[2]]]
        else:
            return mapping


# Read heuristic file
def readHeuristic(fname):
    filedata = open(fname, 'r')
    heuristic = {}

    for h in filedata:
        h = h.lstrip()
        h = h.rstrip()
        if h != 'END OF INPUT':
            data = h.split(' ')
            data[1] = float(data[1])
            heuristic[data[0]] = data[1]
        else:
            return heuristic