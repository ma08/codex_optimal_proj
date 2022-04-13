
n = int(input())
s = input()

t = [""] * n

# Reversing the string
s = s[::-1]

for i in reversed(range(1, n + 1)):
    if n % i == 0:
        # Reversing the substring
        s = s[:i][::-1] + s[i:]

print(s)
