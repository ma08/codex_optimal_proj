

import sys

def main():
    line = sys.stdin.readline()
    d, s, t = line.split()
    s = int(s)
    d = int(d)
    t = int(t)
    if (d / s) <= t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
