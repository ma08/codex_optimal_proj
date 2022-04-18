
n = int(input())
x = list(map(int, input().split()))
print(sum(x) - max(x), sum(x) - min(x))
