

import sys

def main():
    # Read each line
    for line in sys.stdin:
        # Split the line into a list of strings
        line = line.split()
        # Create a set of the list
        line = set(line)
        # Print the length of the set
        print(len(line))

if __name__ == '__main__':
    main()
