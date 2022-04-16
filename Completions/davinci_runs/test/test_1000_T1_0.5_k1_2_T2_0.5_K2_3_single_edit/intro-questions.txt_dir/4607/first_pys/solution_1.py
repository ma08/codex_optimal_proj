

a, b = map(int, input().split())

print(sum(1 for i in range(1, a + 1) if i == int(str(i)[-1])))