import math

def minPowerStrips(A, B):
    return math.ceil(B/A)

def main():
    A, B = map(int, input().split())
    print(minPowerStrips(A, B))

if __name__ == '__main__':
    main()
