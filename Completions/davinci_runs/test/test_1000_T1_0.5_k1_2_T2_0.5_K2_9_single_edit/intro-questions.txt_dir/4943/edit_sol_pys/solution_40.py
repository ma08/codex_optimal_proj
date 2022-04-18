

# Work in progress


def main():
    """
    The main function
    """
    num_corners = int(input().strip()) # number of corners
    corners = []
    for _ in range(num_corners):
        x, y = input().strip().split() # x and y coordinates
        corners.append((float(x), float(y)))
    area = int(input().strip()) # area of the shape
    print(corners)
    print(area)


if __name__ == "__main__":
    main()
