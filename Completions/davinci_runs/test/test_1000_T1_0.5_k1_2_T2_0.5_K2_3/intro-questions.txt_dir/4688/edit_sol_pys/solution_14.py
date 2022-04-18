
s = input()
if s[1:].count(s[0]) == len(s) - 1:
    print("Yes")
else:
    print(-1)
