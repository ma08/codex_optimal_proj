
n, k = map(int, input().split())
print(sum(1 for _ in range(n) if int(input()) >= k))
