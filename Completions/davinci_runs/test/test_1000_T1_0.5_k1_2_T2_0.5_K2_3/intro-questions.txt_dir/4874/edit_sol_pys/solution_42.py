import os
import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            print(line.strip())

if __name__ == '__main__':
    main(sys.argv[1])
