

# Work in progress


def main():
    """
    The main function
    """
    num_corners = int(input().strip())  # number of corners.
    corners = []
    for _ in range(num_corners):
        x, y = input().strip().split()
        corners.append((float(x), float(y)))  # coordinates of corners.
    area = int(input().strip())  # area of the polygon.
    print(corners)
    print(area)


if __name__ == "__main__":
    main()
