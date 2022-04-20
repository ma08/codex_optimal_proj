

# a = input().split()
# a = list(map(int, a))
#
# a.sort()
# print(a)

# a = input().split()
# a = list(map(int, a))
#
# b = input().split()
# b = list(map(int, b))
#
# a = a + b
# a.sort()
# print(a)

a = input().split()
a = list(map(int, a))

b = input().split()
b = list(map(int, b))

c = input().split()
c = list(map(int, c))

a = a + b + c
a.sort()
print(a)