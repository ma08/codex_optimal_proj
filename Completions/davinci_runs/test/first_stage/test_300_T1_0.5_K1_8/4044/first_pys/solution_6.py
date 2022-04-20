

# Solution 1:
# a = input()
# a = a.split(' ')
# a = [int(i) for i in a]
# print(a)
# b = []
# for i in range(0, a[0]):
#     b.append(0)
# for i in range(0, a[1]):
#     b.append(1)
# print(b)
# for i in range(0, a[2]):
#     b[i], b[i+1] = b[i+1], b[i]
# print(b)
# b = ''.join(str(i) for i in b)
# print(b)

# Solution 2:
# a, b, x = map(int, input().split())
# print(a, b, x)
# c = ''
# for i in range(0, a):
#     c += '0'
# for i in range(0, b):
#     c += '1'
# print(c)
# for i in range(0, x):
#     c = c[:i] + c[i+1] + c[i] + c[i+2:]
# print(c)

# Solution 3:
a, b, x = map(int, input().split())
print(a, b, x)
c = []
for i in range(0, a):
    c.append(0)
for i in range(0, b):
    c.append(1)
print(c)
for i in range(0, x):
    c[i], c[i+1] = c[i+1], c[i]
print(c)
c = ''.join(str(i) for i in c)
print(c)