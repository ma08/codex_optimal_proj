

# Solution

s = input()
t = input()

i = 0
j = 0

count = 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
        j += 1
    else:
        count += 1
        j += 1

count += len(s) - i

print(count)