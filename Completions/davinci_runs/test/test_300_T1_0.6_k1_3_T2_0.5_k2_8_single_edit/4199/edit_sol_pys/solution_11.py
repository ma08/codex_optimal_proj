

N, K = map(int, input().split())
H = list(map(int, input().split()))

print(len([x for x in H if x >= K]))
