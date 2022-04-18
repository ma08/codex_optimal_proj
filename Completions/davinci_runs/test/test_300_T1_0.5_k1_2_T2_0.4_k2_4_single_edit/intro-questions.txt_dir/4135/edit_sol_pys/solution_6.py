

n = int(input())
t = input()

s = [""] * n

# reverse the string.
t = t[::-1]

for i in reversed(range(1, n + 1)):
    if n % i == 0:
        # reverse the substring.
        t = t[:i][::-1] + t[i:]

print(t)
