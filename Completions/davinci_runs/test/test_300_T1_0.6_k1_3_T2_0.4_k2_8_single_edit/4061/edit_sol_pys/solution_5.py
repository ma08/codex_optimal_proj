

from sys import stdin, stdout

line = stdin.readline()
s = line.rstrip()

line = stdin.readline()
t = line.rstrip()

i = 0
j = 0
res = 0

while i < len(s):
    if s[i] == t[j]:
        j += 1
        i += 1
    else:
        res += 1
        i += 1

res += len(s) - len(t) - i

stdout.write(str(res))
