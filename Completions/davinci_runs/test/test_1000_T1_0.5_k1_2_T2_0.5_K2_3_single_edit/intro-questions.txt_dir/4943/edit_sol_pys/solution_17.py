

# Work in progress


def main():
    """
    The main function
    """
    num_corners = int(input().strip())
    corners = []
    for _ in range(num_corners):
        x, y = input().strip().split()
        corners.append((float(x), float(y)))
    area = float(input().strip())
    print(corners)
    print(area)


if __name__ == "__main__":
    main()
