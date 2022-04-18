
import sys
import math

def read_input():
    line = sys.stdin.readline()
    return [int(i) for i in line.split()]

def main():
    C, P = read_input()
    heights = read_input()
    max_height = max(heights)

    if P == 0:
        # I
        print(1)
        return

    # I
    if P == 1:
        print(1)
        return

    # S
    if P == 2:
        # horizontal
        if max_height == heights[0]:
            print(1)
            return
        elif max_height == heights[0] + 1:
            print(2)
            return
        else:
            print(3)
            return

    # Z
    if P == 3:
        # horizontal
        if max_height == heights[-1]:
            print(1)
            return
        elif max_height == heights[-1] + 1:
            print(2)
            return
        else:
            print(3)
            return

    # L
    if P == 4:
        # horizontal
        if max_height == 1:
            print(1)
            return
        elif max_height == 2:
            print(2)
            return
        else:
            print(4)
            return

    # J
    if P == 5:
        # horizontal
        if max_height == 1:
            print(1)
            return
        elif max_height == 2:
            print(2)
            return
        else:
            print(4)
            return

    # T
    if P == 6:
        # horizontal
        if max_height == 1:
            print(1)
            return
        elif max_height == 2:
            print(2)
            return
        else:
            print(4)
            return

    # O
    if P == 7:
        print(1)
        return

if __name__ == "__main__":
    main()
