
import sys
import math

def main():
    R, C = map(int, sys.stdin.readline().strip().split())
    total_area = math.pi * pow(R, 2)
    cheese_area = math.pi * pow(R-C, 2)
    print(cheese_area / total_area * 100)

if __name__ == '__main__':
    main()
