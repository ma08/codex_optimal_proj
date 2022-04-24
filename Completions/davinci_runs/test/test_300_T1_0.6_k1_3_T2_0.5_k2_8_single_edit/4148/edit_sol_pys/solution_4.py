
n = int(input())
s = input()

for i in s:
    print(chr(ord(i) + n), end='')

print(s)
