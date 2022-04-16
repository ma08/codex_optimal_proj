
import math
import sys

def read_input():
    line = sys.stdin.readline()
    return [int(i) for i in line.split()][1:]

def main():
    C = read_input()
    P = read_input()
    heights = [0] * C[0]
    max_height = 0

    for i in range(len(P)):
        heights[P[i] - 1] += 1
        max_height = max(max_height, heights[P[i] - 1])

    # print(heights)

    if P == 1:
        # O
        print(1)
        return

    # I
    if P == 2:
        print(1)
        return

    # S
    if P == 3:
        # vertical
        if max_height == heights[0] or max_height == heights[-1]:
            print(1)
            return
        elif max_height == heights[0] + 1 or max_height == heights[-1] + 1:
            print(2)
            return
        else:
            print(3)
            return

    # Z
    if P == 4:
        # vertical
        if max_height == heights[0] or max_height == heights[-1]:
            print(1)
            return
        elif max_height == heights[0] + 1 or max_height == heights[-1] + 1:
            print(2)
            return
        else:
            print(3)
            return

    # L
    if P == 5:
        # vertical
        if max_height == heights[0] or max_height == heights[-1]:
            print(1)
            return
        elif max_height == heights[0] + 1 or max_height == heights[-1] + 1:
            print(2)
            return
        else:
            print(4)
            return

    # J
    if P == 6:
        # vertical
        if max_height == heights[0] or max_height == heights[-1]:
            print(1)
            return
        elif max_height == heights[0] + 1 or max_height == heights[-1] + 1:
            print(2)
            return
        else:
            print(4)
            return

    # T
    if P == 7:
        # vertical
        if max_height == heights[0] or max_height == heights[-1]:
            print(1)
            return
        elif max_height == heights[0] + 1 or max_height == heights[-1] + 1:
            print(2)
            return
        else:
            print(4)
            return

if __name__ == "__main__":
    main()
