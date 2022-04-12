
n = int(input())
d = list(map(int, input().split()))
d.sort(reverse=True)

cnt = 0
for i in range(n//2):
    if d[i] == d[i+n//2]:
        cnt += 1
    else:
        break
print(n//2 + cnt)
