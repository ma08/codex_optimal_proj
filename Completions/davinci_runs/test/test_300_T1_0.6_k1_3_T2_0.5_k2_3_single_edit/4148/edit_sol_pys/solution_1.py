

n = int(input())
s = input()
s = [chr(ord(i) + n) for i in s]
s = ''.join(s)
print(s)
