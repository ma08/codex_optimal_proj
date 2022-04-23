

from sys import stdin

line = stdin.readline()
s = line.rstrip()  # rstrip: 문자열의 오른쪽 공백을 제거

line = stdin.readline()
t = line.rstrip()  # rstrip: 문자열의 오른쪽 공백을 제거

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

print(res)
