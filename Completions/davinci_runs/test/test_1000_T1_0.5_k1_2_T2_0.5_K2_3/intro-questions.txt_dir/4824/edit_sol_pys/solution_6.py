
import sys

def read_input():
    line = sys.stdin.readline()
    return [int(i) for i in line.split()]

def main():
    C, P = read_input()
    heights = read_input()
    max_height = max(heights)

    if P == 1:
        # I - 1
        print(1)
        return

    # I - 1
    if P == 2:
        print(1)
        return

        return

    # S - 3
    if P == 3:
        # horizontal - 1
        if max_height == heights[0]:
            print(1)
            return
        # vertical - 2
        if max_height == heights[0] + 1:
            print(2)
        # vertical - 3
            return
        else:
            print(3)
            return

    # Z - 3
    if P == 4:
        # horizontal - 1
        if max_height == heights[-1]:
            print(1)
            return
        # vertical - 2
        if max_height == heights[-1] + 1:
            print(2)
            return
        else:
        # vertical - 3
            print(3)
            return

    # L - 4
    if P == 5:
        # horizontal - 1
        if max_height == 1:
            print(1)
            return
        # vertical - 2
        if max_height == 2:
            print(2)
            return
        else:
        # vertical - 4
            print(4)
            return

    # J - 4
    if P == 6:
        # horizontal - 1
        if max_height == 1:
            print(1)
            return
        # vertical - 2
        if max_height == 2:
            print(2)
        # vertical - 4
            return
        else:
            print(4)
            return

    # T - 4
    if P == 7:
        # horizontal - 1
        if max_height == 1:
            print(1)
            return
        # vertical - 2
        if max_height == 2:
            print(2)
            return
        else:
        # vertical - 4
            print(4)
            return

if __name__ == "__main__":
    main()
