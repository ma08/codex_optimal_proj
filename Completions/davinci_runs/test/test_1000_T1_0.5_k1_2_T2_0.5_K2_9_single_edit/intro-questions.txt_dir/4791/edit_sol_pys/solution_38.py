n = int(input())
a = list(map(int, input().split()))
if a[0] == 0:
    print(0)
else:
    cnt = 1
    for i in range(1, n):
        if a[i] == 0:
            break
        if a[i] <= a[i - 1]:
            cnt += 1
    print(cnt)
