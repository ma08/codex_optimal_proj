

a, b = map(int, input().split())

print(sum(1 for i in range(a, b + 1) if i == int(str(i)[-1])))
