

n, k = map(int, input().split())

if n < k:
    print("NO")
else:
    a = [1] * k
    while sum(a) != n:
        for i in range(k):
            a[i] += 1
            if sum(a) == n:
                break
    if max(a) > 2 * min(a):
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, a)))