

import sys, math

def main():
    r, c = map(int, sys.stdin.readline().strip().split())
    total_area = math.pi * r**2
    cheese_area = math.pi * (r-c)**2
    print(round(cheese_area / total_area * 100, 6))

if __name__ == '__main__':
    main()
