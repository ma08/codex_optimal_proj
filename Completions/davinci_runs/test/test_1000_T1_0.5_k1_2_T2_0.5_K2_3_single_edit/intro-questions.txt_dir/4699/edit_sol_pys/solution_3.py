
N, K = map(int, input().split())
D = set(map(int, input().split()))

# print(N, K, D)

for i in range(N, 10000):
    if all(d not in str(i) for d in D):
        print(i)
        break
