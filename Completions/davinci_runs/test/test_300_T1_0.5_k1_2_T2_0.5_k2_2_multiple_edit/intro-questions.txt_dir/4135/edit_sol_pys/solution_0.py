
n = int(input())
t = input()

s = [""] * n

# Reverse the string
print(t)
t = t[::-1]

for i in reversed(range(1, n + 1)):
    if n % i == 0:
        # Reverse the substring
        t = t[:i][::-1] + t[i:][::-1]
        print(t)

print(t)
