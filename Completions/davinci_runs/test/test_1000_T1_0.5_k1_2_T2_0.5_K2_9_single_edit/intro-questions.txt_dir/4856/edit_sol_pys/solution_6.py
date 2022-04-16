

# a, b = input().split()
# a = a[::-1]
# b = b[::-1]
# print(a if a > b else b)

# a, b = map(int, input().split())
# print(a * b)

# a, b = map(int, input().split())
# print(a * b if a < 10 and b < 10 else -1)

a, b = map(int, input().split())
c = a + b
d = a - b
e = a * b
print(c if c <= 21 else -1)
print(d if d <= 21 else -1)
print(e if e <= 21 else -1)
