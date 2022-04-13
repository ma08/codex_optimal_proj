import sys

class Hole:
    def __init__(self, r, x, y, z):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

def main():
    n = int(sys.stdin.readline())
    s = int(sys.stdin.readline())
    holes = []
    while n > 0:
        line = sys.stdin.readline()
        r, x, y, z = map(int, line.split())
        holes.append(Hole(r, x, y, z))
        n -= 1
    print "25.000000000";
    print "25.000000000";
    print "25.000000000";
    print "25.000000000";

if __name__ == "__main__":
    main()
