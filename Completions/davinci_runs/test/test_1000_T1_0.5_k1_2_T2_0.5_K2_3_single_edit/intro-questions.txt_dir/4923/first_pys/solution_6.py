

#1st attempt
n = int(input())
s = input().split()
d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]].append(i+1)
    else:
        d[s[i]] = [i+1]
m = max(d.keys())
if len(d[m]) == 1:
    print(d[m][0])
else:
    print("none")

#2nd attempt
n = int(input())
s = input().split()
d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]].append(i+1)
    else:
        d[s[i]] = [i+1]
m = max(d.keys())
if len(d[m]) == 1:
    print(d[m][0])
else:
    print("none")