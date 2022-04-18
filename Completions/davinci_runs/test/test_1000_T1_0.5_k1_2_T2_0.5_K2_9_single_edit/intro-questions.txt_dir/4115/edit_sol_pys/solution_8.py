

s = input().strip()

if s == s[::-1]:
    print(0)
    exit()

for i in range(len(s) // 2 + 1):
    if s[i] == s[-i - 1]:
        continue
    else:
        print(1)
        break
else:
    print(1)
