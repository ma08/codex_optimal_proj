

def main():
    n, m = map(int, input().split())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    segments.sort(key=lambda x: x[0])
    # print(segments)
    # points = []
    # for i in range(n-1):
    #     if segments[i][1] < segments[i+1][0]:
    #         points.append(segments[i][1])
    # print(len(points))
    # print(*points)

if __name__ == "__main__":
    main()
