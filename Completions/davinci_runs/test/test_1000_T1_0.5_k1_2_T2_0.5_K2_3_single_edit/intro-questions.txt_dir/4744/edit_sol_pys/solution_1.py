

import math

def main():
    v = int(input())
    print(find_cost(v)

def find_cost(v):
    cost = math.infinity
    for i in range(1, int(math.sqrt(v)) + 1):
        if v % i == 0:
            if 2 * i + 2 * (v // i) < cost:
                cost = 2 * i + 2 * (v // i)
    return cost

if __name__ == "__main__":
    main()
