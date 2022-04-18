
import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        line = sys.stdin.readline()
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
