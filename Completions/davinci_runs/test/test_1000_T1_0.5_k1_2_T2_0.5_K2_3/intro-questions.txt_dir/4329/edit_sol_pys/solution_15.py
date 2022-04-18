
s = input()
t = input()

if t[-len(s):] == s:
    print('Yes')
else:
    print('No')
