
N, K = map(int, input().split())

fruit = list(map(int, input().split()))
fruit.sort(reverse=True)

print(sum(fruit[:K]))
