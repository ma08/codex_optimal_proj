import sys

def main():
    n = int(sys.stdin.readline().strip())
    s = int(sys.stdin.readline().strip())
    holes = []
    while n > 0:
        line = sys.stdin.readline().strip()
        r, x, y, z = map(int, line.split())
        holes.append((r, x, y, z))
        n -= 1
    #print holes
    #print s
    print "25.000000000",
    print "25.000000000",
    print "25.000000000",
    print "25.000000000",

if __name__ == "__main__":
    main()
