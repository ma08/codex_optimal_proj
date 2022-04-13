

import sys

def main():
    line = sys.stdin.readline()
    a, b = line.split()
    a = int(a)  # convert string to int
    b = int(b)  # convert string to int
    print((a + b) % 24)

if __name__ == '__main__':
    main()
