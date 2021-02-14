# Reads the heuristic file
def readHeuristicfile(fName):
    filedata = open(fName, 'r')
    heu = {}
    for i in filedata:
        i = i.lstrip()
        i = i.rstrip()
        if i != 'END OF INPUT':
            data = i.split(' ')
            data[1] = float(data[1])
            heu[data[0]] = data[1]
        else:
             return heu