
import sys

def main():
    line = sys.stdin.readline()
    d, t, s = line.split()
    d = int(d)
    t = int(t)
    s = int(s)
    if (d / s) <= t: #if distance/speed is less than or equal to time
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
