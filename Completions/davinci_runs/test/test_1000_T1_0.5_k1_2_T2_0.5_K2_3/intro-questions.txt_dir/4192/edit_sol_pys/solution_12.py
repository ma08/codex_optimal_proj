
import sys

def main():
    line = sys.stdin.readline()
    d, s, t = line.split()
    d = int(d)
    s = float(s)
    t = float(t)
    if (d / s) <= t:
        print("Yes") 
    else:
        print("No")

if __name__ == '__main__':
    main()
