# check if it is palindrome
s = input()

if s == s[::-1]:
    print(0)
    exit()
# check if one character needs to be changed
for i in range(len(s) // 2):
    if s[i] == s[-1 - i]:
        continue
    else:
        print(1)
        break
else:
    print(1)
