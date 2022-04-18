import math, sys

def main():
    r, c = map(int, sys.stdin.readline().split())
    area = math.pi * (r**2)
    cheese_area = area - math.pi * ((r-c)**2)
    print(cheese_area / area * 100)

if __name__ == "__main__":
    main()
