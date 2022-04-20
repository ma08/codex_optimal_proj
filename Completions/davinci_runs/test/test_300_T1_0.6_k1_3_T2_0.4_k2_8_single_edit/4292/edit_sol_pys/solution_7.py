
N, K = map(int, input().split())

fruit = list(map(int, input().split()))
print(sum(sorted(fruit)[:K]))
