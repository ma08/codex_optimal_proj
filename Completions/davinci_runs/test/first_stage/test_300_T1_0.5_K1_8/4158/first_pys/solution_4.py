

def solve(n, points):
    points.sort()
    # print(points)
    start = 0
    end = 1
    max_end = 1
    count = 0
    while end < len(points):
        if points[end] - points[start] == 2 ** count:
            count += 1
            end += 1
            max_end = max(max_end, end)
        elif points[end] - points[start] > 2 ** count:
            start += 1
            count = 0
            end = start + 1
        else:
            end += 1
    # print(max_end)
    return points[:max_end]

if __name__ == "__main__":
    n = int(input())
    points = list(map(int, input().split()))
    ans = solve(n, points)
    print(len(ans))
    print(*ans)