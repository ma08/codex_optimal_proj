

a = int(input()) # 1
b = int(input()) # 0
c = int(input()) # 1
d = int(input()) # 0

e = not a # 0
f = not b # 1

g = e or f # 1

h = not c # 0
i = not d # 1

j = h or i # 1

k = g and j # 1

print(int(k))
