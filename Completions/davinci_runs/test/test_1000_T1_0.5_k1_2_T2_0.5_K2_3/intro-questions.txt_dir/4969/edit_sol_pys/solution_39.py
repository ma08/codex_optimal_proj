

import math

def main():
    R, C = map(int, input().split())
    pizza_area = math.pi * (R ** 2)
    cheese_area = pizza_area - math.pi * ((R - C) ** 2)
    print(100 * (cheese_area / pizza_area))

if __name__ == "__main__":

    main()
