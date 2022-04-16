
import math

def main():
    radius, crust = [int(i) for i in input().split(" ")]
    cheese_radius = radius - crust
    cheese_area = math.pi * cheese_radius**2
    total_area = math.pi * radius**2
    print("%.10f" % (cheese_area/total_area * 100))

if __name__ == "__main__":
    main()
