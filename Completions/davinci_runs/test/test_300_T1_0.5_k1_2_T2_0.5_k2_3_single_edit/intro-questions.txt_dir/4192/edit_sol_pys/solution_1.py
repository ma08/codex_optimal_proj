

import sys

def main():
    line = sys.stdin.readline()
    d, t = line.split()
    d = int(d)
    t = int(t)
    if (d / 2) <= t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
