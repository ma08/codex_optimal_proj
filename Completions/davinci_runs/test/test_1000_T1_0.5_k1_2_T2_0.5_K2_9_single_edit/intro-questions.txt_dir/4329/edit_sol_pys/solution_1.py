

s = input()
t = input()

if t[0:len(s)] == s and len(s) < len(t):
    print('Yes')
else:
    print('No')
