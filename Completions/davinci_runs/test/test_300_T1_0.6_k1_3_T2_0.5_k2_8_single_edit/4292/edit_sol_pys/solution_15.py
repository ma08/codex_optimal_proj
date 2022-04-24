

N, K = map(int, input().split())
fruits = sorted(list(map(int, input().split())), reverse=True)
print(sum(fruits[:K]))
