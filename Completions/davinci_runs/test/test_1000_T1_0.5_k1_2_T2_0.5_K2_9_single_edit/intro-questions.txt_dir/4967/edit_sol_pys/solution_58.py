
import sys


def main():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(grid)


if __name__ == "__main__":
    main()


# import sys

# def main():
#     n = int(sys.stdin.readline())
#     grid = [sys.stdin.readline() for _ in range(n)]
#     spy = None
#     safe_houses = []
#     for i in range(n):
#         for j in range(n):
#             if grid[i][j] == 'S':
#                 spy = (i, j)
#             elif grid[i][j] == 'H':
#                 safe_houses.append((i, j))

#     distances = []
#     for house in safe_houses:
#         distances.append(abs(spy[0] - house[0]) + abs(spy[1] - house[1]))
#     print(max(distances))

# if __name__ == "__main__":
#     main()
