
n = int(input())
t = input()

# reverse the string.
t = list(t[::-1])

for i in reversed(range(1, n + 1)):
    if n % i == 0:
        # reverse the substring.
        t[:i] = list(t[:i][::-1])

print("".join(t))
