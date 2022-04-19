

s = input().strip()

if s == s[::-1] or len(s) == 1:
    print(1)
    exit(0)

for i in range(len(s) // 2):
    if s[i] != s[-1 - i]:
        print(1)
        break
    else:
        continue
else:
    print(0)
