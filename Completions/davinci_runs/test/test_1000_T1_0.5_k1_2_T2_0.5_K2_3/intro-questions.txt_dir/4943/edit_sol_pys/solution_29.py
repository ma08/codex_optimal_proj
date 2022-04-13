

# Work in progress.


def main():
    """
    The main function
    """
    num_corners = int(input())
    corners = []
    for _ in range(num_corners):
        x, y = input().split()
        corners.append((float(x), float(y)))
    area = int(input())
    print(corners)
    print(area)


if __name__ == "__main__":
    main()
