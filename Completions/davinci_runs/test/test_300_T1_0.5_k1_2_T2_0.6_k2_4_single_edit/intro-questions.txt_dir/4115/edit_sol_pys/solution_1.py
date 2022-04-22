

s = input()

if s == s[::-1]:
    print(0)
    exit()

for i in range(len(s) // 2):
    if s[i] == s[-1 - i]:
        continue
    print(1)
    exit()
else:
    print(1)
