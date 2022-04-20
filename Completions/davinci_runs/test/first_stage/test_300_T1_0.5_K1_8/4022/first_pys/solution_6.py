
from sys import stdin

def main():
    n = int(stdin.readline())
    points = []
    for _ in range(n):
        l, r = [int(x) for x in stdin.readline().split()]
        points.append((l, 1))
        points.append((r, -1))
    points.sort()
    cnt = 0
    ans = 0
    for i in range(len(points)):
        cnt += points[i][1]
        if cnt == n - 1:
            if i + 1 < len(points):
                ans = max(ans, points[i + 1][0] - points[i][0])
            else:
                ans = max(ans, points[i][0] - points[i - 1][0])
    print(ans)

if __name__ == '__main__':
    main()