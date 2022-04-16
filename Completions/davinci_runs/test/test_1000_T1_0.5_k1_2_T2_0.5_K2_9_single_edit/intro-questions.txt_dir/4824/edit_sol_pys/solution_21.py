import sys


def main(filename):
    lines = readfile(filename)
    printlines(lines)

def readfile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines

def printlines(lines):
    for line in lines:
        print line,

if __name__ == '__main__':
    main(sys.argv[1])
