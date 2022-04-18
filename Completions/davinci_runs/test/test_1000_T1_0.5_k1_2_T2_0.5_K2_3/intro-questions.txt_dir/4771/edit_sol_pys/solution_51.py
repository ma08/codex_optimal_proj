from operator import mul
from functools import reduce


def main():
    n, V = map(int, input().split())
    box_volumes = []
    for _ in range(n):
        box_volumes.append(reduce(mul, map(int, input().split())))
    print(max(box_volumes) - V) 


if __name__ == "__main__":
    main()
