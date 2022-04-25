
n = int(input())
t = input()

# reverse the string.
t = t[::-1]

for i in reversed(range(1, len(t) + 1)):
    if len(t) % i == 0:
        # reverse the substring.
        t = t[:i][::-1] + t[i:]

print(t)
