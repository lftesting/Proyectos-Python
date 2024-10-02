import sys
from tabulate import tabulate
import csv


def main():
    argument_check()
    opening_file()

# expects exactly one command-line argument the name of a csv file
# if the user does not specify one command-line argument use sys.exit
# if the user enters a command that does not end in ".csv" use sys.exit
def argument_check():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

# if the file in the command line argument does not exist use sys.exit
# output a table formated as ASCII art using tabulate (format the table using grid format)
def opening_file():
    pizza=[]
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for i in reader:
                pizza.append(i)
        print(tabulate(pizza,headers="keys",tablefmt="grid"))
                
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__=="__main__":
    main()