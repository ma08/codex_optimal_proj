
import sys

def read_file(filename):
    """This function reads the input file"""
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        return lines


def main():
    """This function runs the whole program"""
    args = sys.argv[1:]
    if len(args) == 1:
        filename = args[0]
        lines = read_file(filename)
        for line in lines:
            print(line)
    else:
        print("Usage: python3 file.py <filename>")


if __name__ == "__main__":
    main()
