


def main():
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    lines.sort()

    # find the maximum length of the intersection
    # if we remove the first segment
    max_length = lines[1][1] - lines[1][0]
    for i in range(2, n):
        if lines[i][0] <= lines[1][1]:
            max_length = max(max_length, lines[i][1] - lines[1][0])

    # find the maximum length of the intersection
    # if we remove the last segment
    max_length = max(max_length, lines[n - 2][1] - lines[n - 2][0])
    for i in range(n - 3, -1, -1):
        if lines[i][1] >= lines[n - 2][0]:
            max_length = max(max_length, lines[n - 2][1] - lines[i][0])

    print(max_length)


if __name__ == '__main__':
    main()