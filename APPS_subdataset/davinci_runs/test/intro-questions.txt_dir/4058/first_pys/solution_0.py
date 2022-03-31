

n, r = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if a[i] == 0:
        found = False
        for j in range(i, i + r):
            if j >= n:
                break
            if a[j] == 1:
                found = True
                cnt += 1
                a[j] = 2
                break
        if not found:
            print(-1)
            exit()
print(cnt)