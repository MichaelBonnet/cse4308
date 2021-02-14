Name                 : Michael Bonnet
UTA ID               : 1001753296
UTA netID            : mab3296
Programming Language : Python
Omega Compatible     : Unknown

How To Run The Code:

    1. Open terminal in a Linux machine, navigate to unzipped project folder

    2. To run an Informed Search, type into the command line and then press enter:

        python find_route.py [input_file.txt] [City_1] [City_2] [heuristic_file.txt]

        For example, using file input1.txt, and trying to find the route from Bremen to Kassel
        using heuristic file h_kassel.txt, type:

        python find_route.py input1.txt Bremen Kassel h_kassel.txt

    3. To run an Uninformed Search, type into the command line and then press enter:

        python find_route.py [input_file.txt] [City_1] [City_2]

        For example, using file input1.txt, and trying to find the route from Bremen to Kassel, type:
        
        python find_route.py input1.txt Bremen Kassel
