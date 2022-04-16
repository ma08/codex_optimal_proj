

import math

def minPowerStrips(A, B):
    return int(math.ceil(B / A))

def main():
    line = input().split()
    A = int(line[0])
    B = int(line[1])
    print(minPowerStrips(A, B))

if __name__ == '__main__':
    main()
