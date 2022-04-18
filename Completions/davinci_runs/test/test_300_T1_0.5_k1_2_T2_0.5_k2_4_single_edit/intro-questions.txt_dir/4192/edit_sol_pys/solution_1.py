

import sys, math

def main():
    line = sys.stdin.readline()
    d, t, s = line.split()
    d = int(d)
    t = int(t)
    s = int(s)
    if math.ceil(d / s) <= t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
