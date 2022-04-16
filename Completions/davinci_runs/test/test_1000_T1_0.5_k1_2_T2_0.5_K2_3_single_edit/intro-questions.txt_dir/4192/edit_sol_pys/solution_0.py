

import sys

def main():
    line = sys.stdin.readline()
    while line:
        d, t, s = line.split()
        d = int(d)
        t = int(t)
        s = int(s)
        if (d / s) <= t:
            print("Yes")
        else:
            print("No")
        line = sys.stdin.readline()

if __name__ == '__main__':
    main()
