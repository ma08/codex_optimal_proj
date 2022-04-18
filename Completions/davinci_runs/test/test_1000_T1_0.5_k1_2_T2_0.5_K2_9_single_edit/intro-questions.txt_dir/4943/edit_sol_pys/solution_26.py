

# Work in progress


def main():
    """
    The main function
    """
    num_corners = int(input().strip())  # type: int
    corners = []
    for _ in range(num_corners):
        x, y = input().strip().split()  # type: str
        corners.append((float(x), float(y)))
    area = int(input().strip())  # type: int
    print(corners)
    print(area)


if __name__ == "__main__":
    main()
