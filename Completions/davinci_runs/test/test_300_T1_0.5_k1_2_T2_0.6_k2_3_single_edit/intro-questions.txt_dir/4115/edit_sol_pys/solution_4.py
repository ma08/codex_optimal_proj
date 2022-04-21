

s = input()

if s == s[::-1]:
    print(0)
    exit()

for i in range(int(len(s) // 2)):
    if s[i] == s[-1 - i]:
        continue
    else:
        print(1)
        break
else:
    print(1)
