

q = int(input())
for _ in range(q):
    k, n, a, b = map(int, input().split())
    if b > k or a > k or b > k - n:
        print(-1)
        continue
    if a > k - n:
        print(n)
        continue
    if b > k - n:
        print(n - (a - b))
        continue
    if a <= b:
        print(k // a)
        continue
    print(n - (a - b) - (k - n - b) // a)