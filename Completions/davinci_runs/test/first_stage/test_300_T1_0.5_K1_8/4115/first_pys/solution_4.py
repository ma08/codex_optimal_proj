

s = input()

if len(s) == 1:
    print(0)
    exit()

ans = 0
for i in range(int(len(s) / 2)):
    if s[i] != s[-i - 1]:
        ans += 1

print(ans)