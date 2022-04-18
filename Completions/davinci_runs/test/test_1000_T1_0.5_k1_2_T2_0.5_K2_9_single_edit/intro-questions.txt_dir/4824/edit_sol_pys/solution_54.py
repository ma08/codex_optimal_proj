
import sys

def read_input():
    line = sys.stdin.readline()
    return [int(i) for i in line.split()][0]

def main():
    P = read_input()
    heights = read_input()
    max_height = max(heights)

    if P == "I":
        # O
        print(1)
        return

    # I
    if P == "O":
        print(1)
        return

    # S
    if P == "S":
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
    if P == "Z":
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
    if P == "L":
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
    if P == "J":
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
    if P == "T":
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
