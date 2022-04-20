


def main():
    n, m = map(int, input().split())
    # n, m = 100, 100
    segments = []
    for i in range(n):
        # l, r = map(int, input().split())
        l, r = 1, 7
        segments.append((l, r))

    # print(segments)
    points = []
    for i in range(1, m+1):
        for segment in segments:
            if i >= segment[0] and i <= segment[1]:
                break
        else:
            points.append(i)

    print(len(points))
    print(' '.join(map(str, points)))


if __name__ == '__main__':
    main()