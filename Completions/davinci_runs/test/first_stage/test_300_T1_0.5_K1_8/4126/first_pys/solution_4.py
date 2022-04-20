

s = input()
n = len(s)
if s == s[::-1] and s[:n//2] == s[:n//2][::-1] and s[n//2+1:] == s[n//2+1:][::-1]:
    print('Yes')
else:
    print('No')