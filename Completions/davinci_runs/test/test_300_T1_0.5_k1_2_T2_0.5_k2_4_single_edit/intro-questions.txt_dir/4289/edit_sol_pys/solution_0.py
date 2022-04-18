import sys
input = sys.stdin.readline
n = int(input())


for i in range(n):
    a = int(input())
    if a % 2 == 0:
        if a % 3 == 0 or a % 5 == 0:
            print("APPROVED")
        else:
            print("DENIED")
    else:
        print("DENIED")


n = int(input())
t, a = map(int, input().split())
h = [int(input()) for i in range(n)]

diff = []
for i in range(n):
    diff.append(abs(t - h[i] * 0.006 - a))

print(diff.index(min(diff)) + 1)
