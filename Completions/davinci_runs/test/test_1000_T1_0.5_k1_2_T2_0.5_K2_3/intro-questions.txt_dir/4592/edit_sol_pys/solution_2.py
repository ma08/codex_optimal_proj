N, K = map(int, input().split())
a = list(map(int, input().split()))

if N == K:
    print(sum(a))
else:
    a.sort(reverse=True)
    print(sum(a[:K]))
