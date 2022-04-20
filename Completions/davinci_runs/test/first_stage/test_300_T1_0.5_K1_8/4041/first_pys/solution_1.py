

# Solution 1

s = input()
t = input()

lst = []

for i in range(len(s)):
    if s[i] in t:
        lst.append(i)

if len(lst) == len(t):
    print(0)
else:
    print(len(s) - max([lst[i+1] - lst[i] for i in range(len(lst)-1)]))

# Solution 2

s = input()
t = input()

lst = []

for i in range(len(s)):
    if s[i] in t:
        lst.append(i)

if len(lst) == len(t):
    print(0)
else:
    print(len(s) - max([lst[i+1] - lst[i] for i in range(len(lst)-1)]))