
import math

def main():
    r, c = map(int, input().split()) # r is radius, c is cheese thickness
    area = math.pi * (r**2) # area of the circle
    cheese_area = area - math.pi * ((r-c)**2) # area of the cheese
    print(cheese_area / area * 100) # percentage of the cheese

if __name__ == "__main__":
    main()
