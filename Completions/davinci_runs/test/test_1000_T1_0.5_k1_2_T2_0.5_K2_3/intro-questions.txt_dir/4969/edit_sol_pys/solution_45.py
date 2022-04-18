
import sys
import math

def main():
    R, C = map(int, sys.stdin.readline().strip().split())
    total_area = math.pi * R ** 2
    cheesecake_area = math.pi * (R - C) ** 2
    print(cheesecake_area / total_area * 100, end='')

if __name__ == '__main__':
    main()
