

n, k = map(int, input().split())  # input: n k
h = [int(input()) for _ in range(n)]  # input: h1 h2 ... hn
print(sum(1 if i >= k else 0 for i in h))
