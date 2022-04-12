import sys

def main():
    n = int(sys.stdin.readline())
    s = float(sys.stdin.readline())
    holes = []
    while n > 0:
        line = sys.stdin.readline()
        r, x, y, z = map(float, line.split())
        holes.append((r, x, y, z))
        n -= 1
    print("%.9f" % (s / 4))
    print("%.9f" % (s / 4))
    print("%.9f" % (s / 4))
    print("%.9f" % (s / 4))

if __name__ == "__main__":
    main()
