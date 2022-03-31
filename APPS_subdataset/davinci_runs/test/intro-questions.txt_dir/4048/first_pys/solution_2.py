

def main():
    """
    >>> main()
    5
    """
    N = int(input())
    r, c = 1, 1

    while r * c < N:
        if r < c:
            r += 1
        else:
            c += 1
    print(r + c - 2)


if __name__ == "__main__":
    main()