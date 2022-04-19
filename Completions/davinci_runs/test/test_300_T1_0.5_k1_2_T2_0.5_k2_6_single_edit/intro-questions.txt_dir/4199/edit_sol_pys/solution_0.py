

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
print(sum(1 if i >= m else 0 for i in a))
