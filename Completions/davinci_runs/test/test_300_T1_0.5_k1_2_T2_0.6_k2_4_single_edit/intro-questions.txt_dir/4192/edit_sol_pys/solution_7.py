

import sys

def main():
    line = sys.stdin.readline()
    a, b, c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    if (a / c) <= b:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
