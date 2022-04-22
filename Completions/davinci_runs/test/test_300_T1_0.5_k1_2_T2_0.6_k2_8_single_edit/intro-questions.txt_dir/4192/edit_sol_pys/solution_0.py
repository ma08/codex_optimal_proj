

import sys

def main():
    line = sys.stdin.readline()
    x, t, s = line.split()
    x = int(x)
    t = int(t) * 60
    s = int(s) * 60
    if (x / s) <= t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
