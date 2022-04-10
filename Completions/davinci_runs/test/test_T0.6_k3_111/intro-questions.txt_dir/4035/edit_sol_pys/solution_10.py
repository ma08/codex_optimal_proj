a, b = map(int, input().split())

for i in range(1, 101):
    if (i * 0.08) == a and (i * 0.1) == b:
        print(i)
        exit()
print(-1)
