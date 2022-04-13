

s = input()  # s is the first string
t = input()  # t is the second string

if s == t:
    print(len(s))
else:
    print(len(s) + len(t) - 2 * len(set(s) & set(t)))
