# Read input file
def readInput(fname):
    filedata = open(fname, 'r')
    _input = {}

    for route in filedata:
        
        # Remove leading/trailing characters
        route = route.lstrip()
        route = route.rstrip()

        # Loop through all the city-to-city routes
        if route != 'END OF INPUT':
            # If we havent reached the end, keep going

            # Tokenize by spaces
            city_segment = route.split(' ')

            # Convert the distance string to float
            city_segment[2] = float(city_segment[2])

            # Handle the forward route (city A -> city B)
            if city_segment[0] in _input:
                _input[city_segment[0]].append( [city_segment[1], city_segment[2]] )
            else:
                _input[city_segment[0]] = [[city_segment[1], city_segment[2]]]

            # Handle the backward route (city B -> city A)
            if city_segment[1] in _input:
                _input[city_segment[1]].append( [city_segment[0], city_segment[2]] )
            else:
                _input[city_segment[1]] = [[city_segment[0], city_segment[2]]]
        else:
            # If END OF INPUT is reached
            return _input

# end readInput()


# Read heuristic file
def readHeuristic(fname):
    filedata = open(fname, 'r')
    heuristic = {}

    for h in filedata:

        # Remove leading/trailing characters
        h = h.lstrip()
        h = h.rstrip()

        # Loop through all heuristic distances
        if h != 'END OF INPUT':
            # If we haven't reached the end, keep going

            # Tokenize by spaces
            data = h.split(' ')

            # Convert heuristic distance string to float
            data[1] = float(data[1])
            heuristic[data[0]] = data[1]
        else:
            # If END OF INPUT is reached
            return heuristic

# end readHeuristic()