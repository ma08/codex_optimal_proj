

n, k = map(int, input().split())
d = set(map(int, input().split()))

# print(n, k, d)

for i in range(N, 10000):
    if all(d not in str(i) for d in D):
        print(i)
        break
