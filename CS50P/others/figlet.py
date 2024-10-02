from pyfiglet import Figlet
figlet = Figlet()

import sys

if len(sys.argv) == 0:
    ...
elif len(sys.argv) == 2:
    figlet.setfons(font= sys.argv[1])
    input("Input: ")
else:
    print("Please type correct number of arguments")
    sys.exit
