import sys
import readinputfile as readInputFiles
import heuristic as heu
import operator
import fringe  as fringeclass

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
        h = heu.readHeuristicfile(sys.argv[4])
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