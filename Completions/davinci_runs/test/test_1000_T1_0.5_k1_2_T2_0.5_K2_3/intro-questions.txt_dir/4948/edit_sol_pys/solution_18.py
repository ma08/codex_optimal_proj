
import sys

def get_prob_1(r, x, y, z, s):
    return 0.0

def get_prob_2(r, x, y, z, s):
    return 0.0

def get_prob_3(r, x, y, z, s):
    return 0.0

def get_prob_4(r, x, y, z, s):
    return 0.0

def get_prob(r, x, y, z, s):
    return 0.0

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
    for i in range(0, 4):
        r, x, y, z = holes[i]
        print get_prob_1(r, x, y, z, s)
        print get_prob_2(r, x, y, z, s)
        print get_prob_3(r, x, y, z, s)
        print get_prob_4(r, x, y, z, s)
        print get_prob(r, x, y, z, s) 

if __name__ == "__main__":
    main()
