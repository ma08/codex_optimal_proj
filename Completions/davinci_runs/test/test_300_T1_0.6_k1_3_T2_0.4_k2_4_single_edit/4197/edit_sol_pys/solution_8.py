
n, k = map(int, input().split())
a = list(map(int, input().split()))[:n]
b = list(map(int, input().split()))[:k]
for i in b:
    a.append(i)
    print(max(a), end=' ')
