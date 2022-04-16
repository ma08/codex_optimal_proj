

    """
    >>> main()
    6 2
    1 2 3 4 5 6
    1
    >>> main()
    6 3
    1 2 3 4 5 6
    2
    >>> main()
    6 4
    1 2 3 4 5 6
    3
    >>> main()
    6 5
    1 2 3 4 5 6
    4
    >>> main()
    6 6
    1 2 3 4 5 6
    5
    >>> main()
    6 7
    1 2 3 4 5 6
    5
    """
def main():
    n, p = [int(x) for x in input().split()]
    distances = [int(x) for x in input().split()]  # noqa

    distances.sort()
    min_distance = distances[0]
    for i in range(1, n):
        if distances[i] - distances[i - 1] < min_distance:
            min_distance = distances[i] - distances[i - 1]

    print(min_distance)

if __name__ == '__main__':
    main()
