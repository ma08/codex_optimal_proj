

s = input()

r = s.count('0')
b = s.count('1')

print(r if r<b else b)