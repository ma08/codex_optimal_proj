

# Work in progress


def main():
    """
    The main function
    """
    num_corners = int(raw_input().strip())  # number of corners
    corners = []
    for _ in range(num_corners):
        x, y = raw_input().strip().split()
        corners.append((float(x), float(y)))  # coordinates of corners
    area = int(raw_input().strip())  # area of the polygon
    print(corners)
    print(area)


if __name__ == "__main__":
    main()
