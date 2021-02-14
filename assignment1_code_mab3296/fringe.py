# Node Generation Structure
class nodeStructure:
    def __init__(self, parent, city, g, d, f, uninformed):
        self.parent = parent
        self.city = city
        self.g = g # g(n) = cost so far to reach n
        self.d = d
        self.f = f # f(n) = g(n) + h(n) [h(n) being the heuristic]
        self.uninformed = uninformed

# end class nodeStructure


# uses map and heuristic to generate next nodes
def expandNode(node, map, heuristic, SearchType):
    # Map out the options to go from the current city
    actions = map[node.city]
    
    # list of to-be-newly-found nodes adjacent to the node being expanded
    next_nodes = []

    # Loop through each option
    for i in actions:
        # Add to g (cost thus far) the distance cost to go to the new city
        cost = node.g + i[1]

        # Add node depending on method being used
        if node.uninformed:
            # If uninformed, do so using no heuristic
            next_nodes.append(nodeStructure(node, i[0], cost, node.d + 1, 0, node.uninformed))
        else:
            # If informed, do so using the heuristic
            next_nodes.append(nodeStructure(node, i[0], cost, node.d + 1, cost + heuristic[i[0]], node.uninformed))
    return next_nodes

# end expandNode()


# Reconstruct route from node
def reconstruct(node, map, SearchType):
    # List of strings that make up the route
    route = []

    # Distance given current node cost thus far
    distance = node.g

    # Loop back from current node through the start of the process
    while node is not None:

        # Hold the node's parent in temp variable
        _parent = node.parent

        # As long as the parent exists,
        if _parent is not None:
            # Generate distances back through the route, 
            # only keeping those that apply to cities in the chain
            steps = (s for s in map[_parent.city] if s[0] == node.city)

            # Capture the distance of the last optimal step taken
            s = next(steps)

            # Add the last optimal step taken to the route
            route.append(_parent.city + " to " + node.city + ", " + str(s[1]) + " km")

        # update current node
        node = _parent
    # end of back loop

    # We added to the route in reverse order, so we should reverse the list of strings
    route.reverse()

    # Printing out the distance and route
    print("distance: " + str(distance) + " km")
    print("route:")
    for segment in route:
        print(segment)

# end reconstruct()
