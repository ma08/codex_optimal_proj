

a = bool(int(input()))
b = bool(int(input()))
c = bool(int(input()))
d = bool(int(input()))

e = not a
f = not b

g = e or f

h = not c
i = not d

j = h or i

k = g and j

print(k)
