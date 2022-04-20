

N = int(input())
d = list(map(int, input().split()))

d_sorted = sorted(d)

# print(d)
# print(d_sorted)

if N%2 == 0:
    d_mid = d_sorted[N//2-1]
    d_mid_next = d_sorted[N//2]
    # print(d_mid, d_mid_next)
    cnt = 0
    for i in range(len(d)):
        if d[i] == d_mid or d[i] == d_mid_next:
            cnt += 1
    print(cnt)
else:
    d_mid = d_sorted[N//2]
    cnt = 0
    for i in range(len(d)):
        if d[i] == d_mid:
            cnt += 1
    print(cnt)