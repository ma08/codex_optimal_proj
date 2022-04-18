

n = int(input())
t = input()

# reverse the string.
t = t[::-1]

for i in range(1, n + 1):
    if n % i == 0:
        # reverse the substring.
        t = t[:i][::-1] + t[i:]

print(t)
