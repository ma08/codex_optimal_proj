
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
print(s)
print(s % (n*m))
