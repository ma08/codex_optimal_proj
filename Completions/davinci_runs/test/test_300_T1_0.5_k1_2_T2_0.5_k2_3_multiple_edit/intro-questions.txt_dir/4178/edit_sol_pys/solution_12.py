#!/usr/bin/env python3


def main():
    n = int(input())
    heights = list(map(int, input().split()))

    for i in range(1, n - 1):
        if heights[i - 1] >= heights[i]:
            heights[i] += 1

    if heights[-2] > heights[-1]:
        heights[-1] += 1

    for i in range(1, n - 1):
        if heights[i - 1] > heights[i]:
            print('No')
            exit()
    print('Yes')


if __name__ == '__main__':
    main()
