
s = input()

if s == s[::-1]:
    print(1)
    exit()

for i in range(len(s) // 2):
    if s[i] == s[-1 - i]:
        continue
    else:
        print(1)
        break
else:
    print(0)
