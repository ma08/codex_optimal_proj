
N, K = map(int, input().split())

fruit = list(map(int, input().split()))
fruit.sort()

print(sum(fruit[:K])
