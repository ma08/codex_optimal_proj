

n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(2)
else:
    max_len = 1
    incr_len = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            incr_len += 1
        else:
            max_len = max(max_len, incr_len)
            incr_len = 1

    max_len = max(max_len, incr_len)
    print(max_len)