
l = []
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    l.append(n % k if n % k else n // k)
print(*l, sep="\n")
