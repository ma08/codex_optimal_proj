

def main():
    """
    Example:
    >>> main()
    SPPSPSPS
    """
    n = int(input())
    xs = [input() for _ in range(2 * n - 2)]
    xs.sort(key=len)
    xs = xs[::-1]
    for i in xs:
        if len(i) == 1:
            print('P', end='')
        else:
            print('S', end='')
    print()

if __name__ == '__main__':
    main()