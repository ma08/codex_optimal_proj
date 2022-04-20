

def main():
    n, m = map(int, input().split())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    segments.sort(key=lambda x: x[0])
    # print(segments)
    points = []
    for i in range(n):
        if i == 0:
            if segments[i][0] != segments[i][1]:
                points.append(segments[i][0])
        else:
            if segments[i-1][1] < segments[i][0]:
                points.append(segments[i-1][1])
    if segments[-1][1] != segments[-1][0]:
        points.append(segments[-1][1])
    print(len(points))
    print(*points)

if __name__ == "__main__":
    main()
