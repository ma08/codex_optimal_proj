
import sys

def main():
    lines = sys.stdin.readlines()
    for line in lines:
        d, t, s = line.split()
        d = int(d)
        t = int(t)
        s = int(s)
        if (d / s) <= t:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
