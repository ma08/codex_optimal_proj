

import math

def main():
    v = int(input())
    print(find_cost(v))

def find_cost(volume):
    cost = math.inf
    for i in range(1, int(math.sqrt(volume)) + 1):
        if volume % i == 0:
            if 2 * i + 2 * (volume // i) < cost:
                cost = 2 * i + 2 * (volume // i)
    return cost


if __name__ == "__main__":
    main()
