

n = int(input())
t = input()

s = [""] * n

# reverse string
t = t[::-1]

for i in reversed(range(1, n + 1)):
    if n % i == 0:
        # reverse substring
        t = t[:i][::-1] + t[i:]

print(t)
