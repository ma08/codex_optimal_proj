
s = input()
s = s.lower()
s = s.replace('a','')
s = s.replace('o','')
s = s.replace('y','')
s = s.replace('e','')
s = s.replace('u','')
s = s.replace('i','')
for i in range(len(s)):
    print('.',end='')
    print(s[i],end='')
print()
