

n = int(input())
s = input().split()
d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]].append(i+1)
    else:
        d[s[i]] = [i+1]
m = max(d.values())
if m == 1:
    print("none")
else:
    for i in d:
        if d[i] == m:
            print(i)
