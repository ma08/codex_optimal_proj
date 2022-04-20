

# s = input()
# t = input()

s = "bbaba"
t = "bb"

l = [0 for _ in range(len(s))]

for i in range(len(s)):
    if s[i] in t:
        l[i] = 1

for i in range(1, len(l)):
    l[i] += l[i - 1]

max_len = 0
for i in range(len(l)):
    for j in range(i, len(l)):
        if l[j] - l[i] + l[i] == len(t):
            max_len = max(max_len, j - i + 1)
print(max_len)