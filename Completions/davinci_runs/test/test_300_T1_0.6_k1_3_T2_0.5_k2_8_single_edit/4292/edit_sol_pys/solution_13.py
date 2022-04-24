

N, K = map(int, input().split())

bamboo = list(map(int, input().split()))
bamboo.sort()

print(sum(bamboo[:K]))
