# -*- coding: utf-8 -*-


def main():
    n = int(input())
    heights = list(map(int, input().split()))

    heights = sorted(heights)

    print(heights[n // 2] - heights[n // 2 - 1])


if __name__ == '__main__':
    main()
