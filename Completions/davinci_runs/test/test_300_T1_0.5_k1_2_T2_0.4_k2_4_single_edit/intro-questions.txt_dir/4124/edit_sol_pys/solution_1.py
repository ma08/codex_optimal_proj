

s = input().split()
t = input().split()

print(len(s) + len(t) - 2 * len(set(s) & set(t)))
