

from sys import stdin

s = stdin.readline().strip()

count = 0
for i in range(len(s)):
    if i==0:
        if s[0]==s[1]:
            count += 1
    elif i==len(s)-1:
        if s[i]==s[i-1]:
            count += 1
    else: 
        if s[i]==s[i-1] or s[i]==s[i+1]:
            count += 1

print(count)
