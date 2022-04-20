
N, K = map(int, input().split())
fruits = sorted(list(map(int, input().split())))
print(sum(fruits[:K]))
