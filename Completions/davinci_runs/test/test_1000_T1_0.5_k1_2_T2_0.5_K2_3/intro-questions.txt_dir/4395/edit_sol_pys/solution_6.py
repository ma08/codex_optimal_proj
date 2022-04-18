

n = int(input())
s = input()

if n % 3 == 0:
    t = "RGB" * (n // 3)

elif n % 3 == 1:
    t = "RGB" * (n // 3)
    t = t[:n - 2] + 'G' + t[n - 1:]

else:
    t = "RGB" * (n // 3)
    t = t[:n - 1] + 'G' + t[n - 1:]

r = 0
for i in range(n):
    if s[i] != t[i]:
        r += 1

print(r)
print(t)
