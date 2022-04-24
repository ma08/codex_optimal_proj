

N, K = map(int, input().split())
h = list(map(int, input().split()))

print(len([x for x in h if x >= K]))
