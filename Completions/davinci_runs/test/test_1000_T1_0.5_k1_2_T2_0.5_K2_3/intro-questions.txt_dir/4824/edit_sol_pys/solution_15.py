
import sys

def read_input():
    line = sys.stdin.readline()
    return [int(i) for i in line.split()]

def main():
    C, P = read_input()
    heights = read_input()
    max_height = max(heights)

    if P == 1:
        # O
        print(1)
        return

    # I, S, Z
    if P == 2 or P == 3 or P == 4:
        # verticals
        if max_height == heights[-1]:
        print(1)
        elif max_height == heights[-1] + 1:
            print(2)
        else:
            print(3)

    # L, J, T
    if P == 5 or P == 6 or P == 7:
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
