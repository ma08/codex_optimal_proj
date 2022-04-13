

import sys

def read_input():
    line = sys.stdin.readline()
    return [int(i) for i in line.split(" ")]

def main():
    C, P = read_input()
    print(C, P, heights)
    heights = read_input()
    max_height = max(heights)

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
        # verticals
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
    if P == 4:
        # verticals
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
    if P == 5:
        # verticals
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
    if P == 6:
        # verticals
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
    if P == 7:
        # verticals
        if max_height == 1:
            print(1)
            return
        elif max_height == 2:
            print(2)
            return
        else:
            print(4)
            return

if __name__ == "__main__":
    main()
