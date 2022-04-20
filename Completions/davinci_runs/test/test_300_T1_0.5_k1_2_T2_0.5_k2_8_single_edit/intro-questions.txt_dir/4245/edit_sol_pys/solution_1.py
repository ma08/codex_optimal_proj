
import math

def minPowerStrips(A, B):
    return math.ceil(B / A)

def main():
    print(minPowerStrips(int(input()), int(input())))

if __name__ == '__main__':
    main()
