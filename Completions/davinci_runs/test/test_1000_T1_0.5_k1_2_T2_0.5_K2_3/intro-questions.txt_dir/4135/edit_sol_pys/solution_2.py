

n = int(input())
t = input()

# Reversing the string
t = t[::-1]

for i in range(1, n + 1):
    if n % i == 0 and i < n:
        t = t[:i][::-1] + t[i:] # Reversing the substring

print(t)
