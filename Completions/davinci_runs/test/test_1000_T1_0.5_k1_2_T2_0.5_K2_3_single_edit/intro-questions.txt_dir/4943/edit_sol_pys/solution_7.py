
import math
# Work in progress


def main():
    """
    The main function
    """
    num_corners = int(raw_input().strip())
    corners = []
    for _ in range(num_corners):
        x, y = raw_input().strip().split()
        corners.append((float(x), float(y)))
    area = int(raw_input().strip())
    print(corners, area)
    for corner in corners:
        print(corner[0])
        print(corner[1])


if __name__ == "__main__":
    main()
