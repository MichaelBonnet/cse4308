# Name       : Michael Bonnet
# UTA ID #   : 1001753296
# UTA netID  : mab3296
# Class      : CSE 4308-002 Artificial Intelligence
# Instructor : Vamsikrishna Gopikrishna


# import statements
import sys           # for reading command line arguments
import operator      # because I need operator.attrgetter()
import read as read  # holds the file reading functions
import fringe as fr  # holds the fringe-related functions and node structure


# Main
def main():
    
	# Check if doing informed or uninformed search
    if len(sys.argv) == 5:
        uninformed = False  # If we have five CL args, we have a heuristic file, so we're doing informed
    else:
        uninformed = True   # If we do not have five CL args, are doing uninformed

    # Ensure there is actually input
    if len(sys.argv) != 1:
       map = read.readInput(sys.argv[1])  # If so, read the input
    else:
        print("No input file present")    # If not, abort mission
        sys.exit()

    # Tracking fringe statistics
    nodesExpanded  = 0   # Number of nodes expanded thus far
    nodesGenerated = 0   # Number of nodes generated thus far

    # Holding structure for the heuristic
    heuristic = {}

    # If an informed search, get the heuristic
    if not uninformed:
        heuristic = read.readHeuristic(sys.argv[4])

    # fringe list started
    fringe = []

    if uninformed:
        # If doing an uninformed search, start the fringe without the heuristic guide
        fringe.append(fr.nodeObject(None, sys.argv[2], 0, 0, 0, uninformed))
        nodesGenerated += 1 # We've just generated our first node, manually
    else:
        # If doing an informed search, start the fringe with the heuristic guide
        fringe.append(fr.nodeObject(None, sys.argv[2], 0, 0, heuristic[sys.argv[2]], uninformed))
        nodesGenerated += 1 # We've just generated our first node, manually

    # list of closed nodes/unsuccessful cities
    closed = []
    
    # search loop
    while len(fringe) > 0:
        # Increment the number of nodes expanded
        nodesExpanded += 1
        
        # Pop node
        node = fringe.pop(0)

        # if node.city != goal city
        if node.city != sys.argv[3]:
            # Then we must expand yet again
            if node.city not in closed:
                # Add it to list of unsuccessful cities
                closed.append(node.city)

                # Expand subsequent node(s), populate list of new nodes
                next_node = fr.expandNode(node, map, heuristic, nodesExpanded)

                # For each new node, append it to the fringe
                for i in next_node:
                    fringe.append(i)

                # Increment nodesGenerated by number of new nodes generated
                nodesGenerated += len(next_node)

                if uninformed:
                    # Sort the fringe by cost so far
                    fringe = sorted(fringe, key=operator.attrgetter('g'))
                else:
                    # Sort the cost by fringe with heuristic in mind
                    fringe = sorted(fringe, key=operator.attrgetter('f'))

        # if node.city == goal city
        else:
            # Then we're done
            print("nodes expanded: "  + str(nodesExpanded))
            print("nodes generated: " + str(nodesGenerated))
            fr.backtrace(node, map, nodesExpanded)
            sys.exit() # had to do this because otherwise it would keep looping weirdly
    # end search loop

    # if the length of fringe reaches zero, we have an impossible route.
    else:
    	print("nodes expanded: "  + str(nodesExpanded))
    	print("nodes generated: " + str(nodesGenerated))
    	print("distance: infinity")
    	print("route: \nnone")

# end main()


# Invoke main()
main()
