

a = int(input())
b = int(input())
c = int(input())
d = int(input())

e = a == 0
f = b == 0

g = not e
h = not f

i = g and h

j = c == 0
k = d == 0

l = not j
m = not k

n = l and m

o = i or n

print(int(o))
