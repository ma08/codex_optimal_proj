

import itertools

def main():
    n = int(input())
    tiles = [list(map(int, input().split())) for _ in range(n-1)]

    print(tiles)

if __name__ == "__main__":
    main()
