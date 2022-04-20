

n, k = map(int, input().split())
t = input()

if k < n:
    print(t[:k])
else:
    k -= n
    print(t + t[:k])