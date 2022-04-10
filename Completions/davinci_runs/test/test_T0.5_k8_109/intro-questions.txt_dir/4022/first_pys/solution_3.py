

import sys


def main():
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    segments.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            ans = max(ans, segments[i][1] - segments[i + 1][0])
        elif i == n - 1:
            ans = max(ans, segments[i - 1][1] - segments[i][0])
        else:
            ans = max(ans, segments[i - 1][1] - segments[i + 1][0])
            ans = max(ans, segments[i][1] - segments[i + 1][0])
            ans = max(ans, segments[i - 1][1] - segments[i][0])
    print(ans)


if __name__ == '__main__':
    main()