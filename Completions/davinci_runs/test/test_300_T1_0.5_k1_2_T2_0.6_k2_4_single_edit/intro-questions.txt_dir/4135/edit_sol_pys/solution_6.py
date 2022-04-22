

n = int(input())
t = input()

s = [""] * n

for i in reversed(range(1, n + 1)):
    if n % i == 0:
        # reverse the substring
        t = t[:i] + t[i:][::-1]

print(t)
