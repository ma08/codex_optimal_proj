

n, x = map(int, input().split())
l = list(map(int, input().split()))

cnt = 1
for i in range(n):
    if cnt > x:
        break
    cnt += l[i]

print(i+1)