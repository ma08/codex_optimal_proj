

s = input()
t = input()

if s == t:
    print(0)
else:




    print(len(s) + len(t) - 2*len(set(s) & set(t)))
