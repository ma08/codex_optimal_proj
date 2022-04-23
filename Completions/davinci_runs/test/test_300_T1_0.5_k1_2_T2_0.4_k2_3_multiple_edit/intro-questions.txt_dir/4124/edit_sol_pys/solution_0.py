
s = input()  # s = "abcd"
t = input()  # t = "abcde"

if s == t:
    print(len(s))
else:
    print(len(s) + len(t) - 2 * len(set(s) & set(t)))  # set(s) & set(t) = set(["a", "b", "c"])
