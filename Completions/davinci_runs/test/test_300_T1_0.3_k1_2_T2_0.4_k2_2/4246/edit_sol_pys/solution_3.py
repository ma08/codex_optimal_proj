
s = input()
t = input()
count = 0
for i in range(3):  # i = 0, 1, 2
    if s[i] == t[i]:
        count += 1
print(count)
