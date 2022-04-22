
import sys

def main():
    line = sys.stdin.readline()
    d, t, s = [int(x) for x in line.split()]
    d = int(d)
    t = int(t)
    s = int(s)
    if d / s <= t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
