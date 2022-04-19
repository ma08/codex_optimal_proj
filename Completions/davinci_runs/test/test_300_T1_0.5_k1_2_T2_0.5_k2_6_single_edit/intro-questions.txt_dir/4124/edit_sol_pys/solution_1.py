
s = input()
t = input()

if s == t:
    print(len(s) - 1)
else:
    print(len(s) + len(t) - 2 * len(set(s) & set(t)) - 1)
