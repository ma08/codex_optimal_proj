

s = input()
t = input()

if t[0:len(s)] == s and len(t) == len(s) + 1:
    print('Yes')
else:
    print('No')
