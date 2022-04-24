n = int(input())
a = list(map(int, input().split()))
print(a.index(max(a)) - a.index(min(a)))
