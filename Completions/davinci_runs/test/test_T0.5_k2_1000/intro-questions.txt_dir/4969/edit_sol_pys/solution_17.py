
import math

def main():
    r, c = map(int, input().split())
    pizza_area = math.pi * (r ** 2)
    cheese_area = pizza_area - math.pi * ((r - c) ** 2)
    print(cheese_area / pizza_area * 100)

if __name__ == "__main__":
    main()
