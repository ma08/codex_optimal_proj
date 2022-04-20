

s = input() # 3 <= len(s) <= 99

if s == s[::-1] and s[:len(s)//2] == s[:len(s)//2][::-1] and s[len(s)//2+1:] == s[len(s)//2+1:][::-1]:
    print('Yes')
else:
    print('No')