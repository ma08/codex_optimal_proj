
n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
print(sum([1 for i in h if i >= k]))
