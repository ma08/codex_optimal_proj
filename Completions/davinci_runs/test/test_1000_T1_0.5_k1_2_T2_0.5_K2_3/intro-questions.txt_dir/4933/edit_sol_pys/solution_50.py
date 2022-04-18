

import sys

def main(argv):
    filename = argv[1]
    with open(filename, 'r') as f:
        print f.read()

if __name__ == '__main__':
    main(sys.argv)
