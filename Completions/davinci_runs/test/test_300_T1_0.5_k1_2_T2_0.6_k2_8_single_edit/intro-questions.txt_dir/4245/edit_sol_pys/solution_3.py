import math
import sys

def minPowerStrips(A, B):
    return math.ceil(B / A)

def main():
    line = sys.stdin.readline().split()
    A = int(line[0])
    B = int(line[1])
    print(minPowerStrips(A, B))

if __name__ == '__main__':
    main()
