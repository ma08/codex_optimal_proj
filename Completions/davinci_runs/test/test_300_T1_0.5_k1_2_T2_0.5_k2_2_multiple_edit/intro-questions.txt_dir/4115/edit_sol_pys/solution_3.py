
s = input()

if s == s[::-1]:
    print(0)
    exit()
for i in range(len(s) - 1):
    if s[i] == s[-1 - i] and s[i + 1] == s[-2 - i]:
        continue
    else:
        print(2)
        break
else:
    print(1)
