

s = input()

if s == s[::-1]:  # s == reversed(s)
    print(0)
    exit()

for i in range(len(s) // 2):  # len(s) // 2 == len(s) / 2
    if s[i] == s[-1 - i]:  # s[-1 - i] == s[len(s) - 1 - i]
        continue
    else:
        print(1)
        break
else:
    print(1)
