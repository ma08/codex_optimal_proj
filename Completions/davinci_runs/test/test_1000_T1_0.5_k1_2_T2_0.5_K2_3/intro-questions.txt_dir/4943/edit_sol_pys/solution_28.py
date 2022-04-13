

from math import hypot


def main():
    """
    The main function
    """
    num_corners = int(input().strip())
    corners = []
    for _ in range(num_corners):
        x, y = input().strip().split()
        corners.append((float(x), float(y)))
    area = int(input().strip())
    # print(corners)
    # print(area)
    print(corners[0])


if __name__ == "__main__":
    main()
