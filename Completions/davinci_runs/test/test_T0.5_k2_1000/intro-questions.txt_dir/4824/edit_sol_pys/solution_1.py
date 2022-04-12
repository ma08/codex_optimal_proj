
import sys

def read_input():
    return [int(i) for i in sys.stdin.readline().split()]

def main():
    C, P = read_input()
    max_height = max(read_input())

    if P == 1:
        # I
        print(1)
        return

    # O
    if P == 2:
        print(1)
        return

    # S
    if P == 3:
        # vertical
        if max_height == C:
            print(1)
            return
        elif max_height == C + 1:
            print(2)
            return
        else:
            print(3)
            return

    # Z
    if P == 4:
        # vertical
        if max_height == C:
            print(1)
            return
        elif max_height == C + 1:
            print(2)
            return
        else:
            print(3)
            return

    # L
    if P == 5:
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
    if P == 6:
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
    if P == 7:
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
