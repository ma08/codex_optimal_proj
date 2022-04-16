
import sys

def read_input():
    line = sys.stdin.readline()
    return [int(i) for i in line.split()]  # list comprehension

def main():
    C, P = read_input()
    heights = read_input()
    max_height = max(heights)

    if P == 1:  # O
        # O
        print(1)
        return

    if P == 2:  # I
        print(1)
        return

        return

    if P == 3:  # S
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

    if P == 4:  # Z
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

    if P == 5:  # L
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

    if P == 6:  # J
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

    if P == 7:  # T
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
