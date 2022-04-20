

import sys

def main():
    l, r = map(int, sys.stdin.readline().split())
    # L \leq i < j \leq R
    # 2020 \leq i < j \leq 2040
    # i = 2020, 2039, 2040
    # j = 2021, 2040
    # i * j = 2, 83, 2040
    # i * j % 2019 = 2, 83, 0
    # min(2, 83, 0) = 2
    print(min([(i * j) % 2019 for i in range(l, r + 1) for j in range(i + 1, r + 1)]))

if __name__ == "__main__":
    main()