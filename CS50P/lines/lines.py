import sys

def main():
    argument_check()
    line_count()


def argument_check():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

def line_count():
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
            actual_lines = count_lines(lines)
            print(actual_lines)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def count_lines(lines):
    total_lines = 0
    for line in lines:
        if not line.lstrip().startswith("#") and not line.strip() == "":
            total_lines += 1
    return total_lines


if __name__== "__main__":
    main()
