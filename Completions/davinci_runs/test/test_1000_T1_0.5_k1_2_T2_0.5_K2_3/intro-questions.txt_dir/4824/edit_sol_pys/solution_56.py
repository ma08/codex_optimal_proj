

import sys

def read_input():
    line = sys.stdin.readline()
    return [int(i) for i in line.split()]

def main():
    C, P = read_input()
    heights = read_input()
    max_height = max(heights)

    if P == 1:
        # O (square)
        print(1)
        return

    # I
    elif P == 2:
        print(1)
        return

    # S
    elif P == 3:
        # vertical
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
    elif P == 4:
        # vertical
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
    elif P == 5:
        # vertical
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
    elif P == 6:
        # vertical
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
    elif P == 7:
        # vertical
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
