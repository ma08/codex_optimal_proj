

import sys

def main():
    line = sys.stdin.readline()
    x, y, z = line.split()
    x = int(x)
    y = float(y)
    z = int(z)
    if x / z <= y:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
