

n = int(input())
s = input()

c = [1] * n

last = s[0]

last_color = 1

for i in range(1, n):
    if s[i] > last:
        last_color += 1
    else:
        last_color = 1
    c[i] = last_color
    last = s[i]

print(max(c))
print(*c)
