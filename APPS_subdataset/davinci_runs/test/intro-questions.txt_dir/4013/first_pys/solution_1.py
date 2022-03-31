

n = int(input())
a = list(map(int, input().split()))

print(max(a) - min(a) - 2 * min(max(a) - a.index(max(a)) - 1, a.index(min(a)) - min(a)))