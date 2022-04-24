import sys

s = input()
t = input()

if s == t:
    sys.stdout.write(len(s))
else:
    sys.stdout.write(len(s) + len(t) - 2 * len(set(s) & set(t))) 
