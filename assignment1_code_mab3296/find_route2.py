import sys
import operator
import fringe  as fringeclass


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


# Node Structure
class nodestructure:
    def __init__(self, prnt, state, g, d, f, Uninformed):
        self.prnt = prnt
        self.state = state
        self.g = g
        self.d = d
        self.f = f
        self.Uninformed = Uninformed


    def __str__(self):
        if self.Uninformed:
            return self.state+": g(n)= "+str(self.g) + ",d= "+str(self.d)+",Parent ->{"+str(self.prnt)+"}"
        else:
            return self.state+": g(n)="+str(self.g)+",d= "+str(self.d)+", f(n) = "+str(self.f)+", Parent ->{"+str(self.prnt)+"}"


 # uses map and heuristic to generate successors
def expandNode(node, map, h, SearchType):
    actions = map[node.state]
    successor = []
    for i in actions:
        costtotal = node.g + i[1]
        if node.Uninformed:
            successor.append(nodestructure(node, i[0], costtotal, node.d + 1, 0, node.Uninformed))
        else:
            successor.append(nodestructure(node, i[0], costtotal, node.d + 1, costtotal + h[i[0]], node.Uninformed))
    return successor


def getkey(item,n):
    return item[n]


# reconstruct the path from node
def reconstruct(node, map,SearchType):
    s = []
    distance = node.g
    while node is not None:
        parent = node.prnt
        if parent is not None:
            act = (a for a in map[parent.state] if
                   a[0] == node.state)
            a=next(act)
            s.append(parent.state+" to "+node.state+ ", "+str(a[1])+" kms")
        node = parent
    s.reverse()
    print("distance : " + str(distance))
    print("route :")
    for i in s:
        print(i)


# Main function/heavy lifting
def main():
    if len(sys.argv) == 5:
        print("Informed Search")
        Uninformed = False
    else:
        print("Uninformed search")
        Uninformed = True
    if len(sys.argv) != 1 :
       map = readInputFiles.readInputFiles(sys.argv[1])
    else:
        print("No input file present")
        sys.exit()
    NoExp = 0
    maxFringe = 0
    Noofgen = 0
    h = {}
    if not Uninformed:
        h = readHeuristicfile(sys.argv[4])
    # fringe started
    fringe = []
    if Uninformed:
        fringe.append(fringeclass.nodestructure(None, sys.argv[2], 0, 0, 0, Uninformed))
    else:
        fringe.append(fringeclass.nodestructure(None, sys.argv[2], 0, 0, h[sys.argv[2]], Uninformed))
    closed = []
    if len(fringe) > maxFringe:
        maxFringe = len(fringe)
       # search loop
    while len(fringe) > 0:
        print("Fringe:")
        print(fringeclass.getkey(fringe,len(fringe)-1))
        print("Closed:")
        print(closed)
        NoExp = NoExp + 1
         # take node
        node = fringe.pop(0)
        # goal state checked
        if node.state != sys.argv[3]:
            if node.state not in closed:
                closed.append(node.state)
                successor = fringeclass.expandNode(node, map, h,NoExp)
                for i in successor:
                    fringe.append(i)
                Noofgen = Noofgen + len(successor)

                if Uninformed:
                    fringe = sorted(fringe, key=operator.attrgetter('g'))
                else:
                    fringe = sorted(fringe, key=operator.attrgetter('f'))

                if len(fringe) > maxFringe:
                    maxFringe = len(fringe)
        else:
            print("Output Generated:")
            print("Nodes Expanded: " + str(NoExp))
            print("Nodes Generated: " + str(Noofgen))
            print("max size of fringe: " + str(maxFringe))
            fringeclass.reconstruct(node, map,NoExp)
            sys.exit()

    else:
        print("Fringe Empty. Goal Not Found. Generating Output")
    print("Nodes Expanded: " + str(NoExp))
    print("Nodes Generated: " + str(Noofgen))
    print("max size of fringe: " + str(maxFringe))
    print("Distance: infinity")
    print("Route: none")

if __name__ == "__main__":
    main()