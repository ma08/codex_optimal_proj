

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

if x < k:
    print(-1)
else:
    # print('a', a)
    # print('n', n)
    # print('k', k)
    # print('x', x)
    # print()
    ans = 0
    for i in range(n - k + 1):
        # print('i', i)
        # print('a[i:i+k]', a[i:i+k])
        # print('max(a[i:i+k])', max(a[i:i+k]))
        # print('a.index(max(a[i:i+k]))', a.index(max(a[i:i+k])))
        # print('a.index(max(a[i:i+k])) + i', a.index(max(a[i:i+k])) + i)
        ans += max(a[i:i+k])
        a[a.index(max(a[i:i+k])) + i] = 0
        # print('a', a)
        # print()
    print(ans)