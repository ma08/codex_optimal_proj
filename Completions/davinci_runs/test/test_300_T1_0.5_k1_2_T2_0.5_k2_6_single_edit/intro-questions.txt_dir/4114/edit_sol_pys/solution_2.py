import sys
input = sys.stdin.readline


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for x in range(101):
    for y in range(101):
        H = 0
        for a in A:
            if a[2] != 0:
                H = a[2] + abs(a[0] - x) + abs(a[1] - y)
                break
        if all(a[2] == max(H - abs(a[0] - x) - abs(a[1] - y), 0) for a in A):
            print(x, y, H)
            exit()
