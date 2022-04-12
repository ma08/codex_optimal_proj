
import sys

def get_prob(r, x, y, z, s):
    return 0.25  # TODO: implement

def main():
    n = int(sys.stdin.readline())
    s = int(sys.stdin.readline())
    holes = []
    while n > 0:
        line = sys.stdin.readline()
        r, x, y, z = map(int, line.split())
        holes.append((r, x, y, z))
        n -= 1
    #print holes
    #print s
    for hole in holes:
        print get_prob(hole[0], hole[1], hole[2], hole[3], s)

if __name__ == "__main__":
    main()
