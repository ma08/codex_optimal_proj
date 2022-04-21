

import sys

def main():
    line = sys.stdin.readline()
    l, x, y, s, d = line.split()
    l = int(l)
    x = int(x)
    y = int(y)
    s = int(s)
    d = int(d)
    if (l / s) <= (d / y):
        print("Yes")
    else:
        print(l / s)
        print(d / y)
        print("No")

if __name__ == '__main__':
    main()
