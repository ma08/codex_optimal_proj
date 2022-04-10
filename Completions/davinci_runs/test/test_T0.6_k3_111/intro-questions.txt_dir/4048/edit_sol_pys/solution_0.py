
def main():
    """
    >>> main(3)
    2
    >>> main(10)
    3
    >>> main(100)
    9
    >>> main(1)
    0
    """
    N = int(input())  # 入力値
    r, c = 1, 1

    while r * c < N:  # 縦横のマス目を増やしていく
        if r < c:
            r += 1
        else:
            c += 1
    print(r + c - 2)


if __name__ == "__main__":
    main()
