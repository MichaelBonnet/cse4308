# import statements
import sys
import operator
import read as read
import fringe as fr


# Main
def main():
    
	# Check if doing informed or uninformed search
    if len(sys.argv) == 5:
        Uninformed = False  # If we have five CL args, we have a heuristic file, so we're doing informed
    else:
        Uninformed = True   # If we do not have five CL args, are doing uninformed

    # Ensure there is actually input
    if len(sys.argv) != 1:
       map = read.readInput(sys.argv[1])  # If so, read the input
    else:
        print("No input file present")    # If not, abort mission
        sys.exit()

    nodesExpanded  = 0
    maxFringe      = 0
    nodesGenerated = 0
    h              = {}

    if not Uninformed:
        h = read.readHeuristic(sys.argv[4])

    # fringe started
    fringe = []

    if Uninformed:
        fringe.append(fr.nodestructure(None, sys.argv[2], 0, 0, 0, Uninformed))
    else:
        fringe.append(fr.nodestructure(None, sys.argv[2], 0, 0, h[sys.argv[2]], Uninformed))

    closed = []

    if len(fringe) > maxFringe:
        maxFringe = len(fringe)
    
    # search loop
    while len(fringe) > 0:
        nodesExpanded = nodesExpanded + 1
        # take node
        node = fringe.pop(0)
        # goal state checked
        if node.state != sys.argv[3]:
            if node.state not in closed:
                closed.append(node.state)
                successor = fr.expandNode(node, map, h,nodesExpanded)

                for i in successor:
                    fringe.append(i)

                nodesGenerated = nodesGenerated + len(successor)

                if Uninformed:
                    fringe = sorted(fringe, key=operator.attrgetter('g'))
                else:
                    fringe = sorted(fringe, key=operator.attrgetter('f'))

                if len(fringe) > maxFringe:
                    maxFringe = len(fringe)
        else:
            print("nodes expanded: " + str(nodesExpanded))
            print("nodes generated: " + str(nodesGenerated))
            # print("max size of fringe: " + str(maxFringe))
            fr.reconstruct(node, map,nodesExpanded)
            sys.exit()
    # end search loop

    else:
    	print("nodes expanded: " + str(nodesExpanded))
    	print("nodes generated: " + str(nodesGenerated))
    	print("distance: infinity")
    	print("route: \nnone")

if __name__ == "__main__":
    main()