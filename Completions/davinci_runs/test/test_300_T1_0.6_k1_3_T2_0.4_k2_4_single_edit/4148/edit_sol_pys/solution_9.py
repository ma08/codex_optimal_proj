
n = int(input())
s = input()

print(''.join(chr(ord(x) + n) for x in s))
