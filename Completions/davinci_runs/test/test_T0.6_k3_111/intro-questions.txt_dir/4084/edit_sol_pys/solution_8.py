
n, a, b = map(int, input().split())

blue = 0
for i in range(min(n, a + 1), 0, -1):
    if i == a:
        blue = i
        break
    else:
        blue = i

print(blue)
