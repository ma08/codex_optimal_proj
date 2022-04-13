import sys



def read_input():
    line = sys.stdin.readline()
    return [int(i) for i in line.split()]


def main():
    C, P = read_input()
    heights = [0] + read_input() + [0]

    if P == 1:
        # O (1)
        print(max(heights[1], heights[2]))
        return

    if P == 2:
        # I (1)
        print(max(heights[1], heights[2], heights[3]))
        return

    if P == 3:
        # S (3)
        print(max(heights[1], heights[2] + 1, heights[3] + 1))
        return

    if P == 4:
        # Z (3)
        print(max(heights[1] + 1, heights[2], heights[3] + 1))
        return

    if P == 5:
        # L (4)
        print(max(heights[1], heights[2], heights[3], heights[4]))
        return

    if P == 6:
        # J (4)
        print(max(heights[1], heights[2], heights[3], heights[4]))
        return

    if P == 7:
        # T (4)
        print(max(heights[1], heights[2], heights[3], heights[4]))
        return


if __name__ == "__main__":
    main()
