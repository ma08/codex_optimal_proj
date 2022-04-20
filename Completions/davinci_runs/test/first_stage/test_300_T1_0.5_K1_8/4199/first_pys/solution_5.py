

N, K = map(int, input().split())
h = list(map(int, input().split()))

print(sum([1 for i in h if i >= K]))