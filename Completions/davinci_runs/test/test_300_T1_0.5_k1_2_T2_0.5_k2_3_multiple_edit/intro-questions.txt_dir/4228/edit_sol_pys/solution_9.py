
n, l = map(int, input().split())
apples = [l + i for i in range(n)]

print(sum(apples) - min([abs(f) for f in apples]))
