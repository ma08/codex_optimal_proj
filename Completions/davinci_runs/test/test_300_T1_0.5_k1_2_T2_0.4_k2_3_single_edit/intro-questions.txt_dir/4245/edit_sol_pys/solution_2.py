import math

def minPowerStrips(a, b):
    return math.ceil(b / a)

def main():
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    print(minPowerStrips(a, b))

if __name__ == '__main__':
    main()
