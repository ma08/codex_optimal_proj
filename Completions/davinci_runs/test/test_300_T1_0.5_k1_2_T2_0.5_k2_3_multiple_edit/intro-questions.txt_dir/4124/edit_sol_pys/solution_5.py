

s = input().strip()
t = input().strip()

if s == t:
    print(len(s))
else:
    print(len(s) + len(t) - 2 * len(set(s) & set(t))
