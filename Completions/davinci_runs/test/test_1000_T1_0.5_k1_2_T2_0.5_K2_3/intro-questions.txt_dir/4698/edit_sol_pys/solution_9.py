import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
m = int(input())
p_x = [list(map(int,input().split())) for _ in range(m)]

for i in range(m):
    p, x = p_x[i]
    print(sum(t) - t[p-1] + x)
