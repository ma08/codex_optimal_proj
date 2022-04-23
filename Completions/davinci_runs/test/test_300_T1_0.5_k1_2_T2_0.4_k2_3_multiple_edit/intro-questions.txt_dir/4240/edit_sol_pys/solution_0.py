s = input()
t = input()

if s == t:
    print("Yes")
    exit()

for i in range(len(s)):
    s = s[-1] + s[:-1] # s[-1] : 最後の文字
    if s == t:
        print("Yes")
        exit()

print("No")
