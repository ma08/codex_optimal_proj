
import math

def minPowerStrips(A, B):   # A is the power of one strip, B is the total power needed
    return math.ceil(B / A)

def main():
    line = input().split()
    A = int(line[0])
    B = int(line[1])
    print(minPowerStrips(A, B))

if __name__ == '__main__':
    main()
