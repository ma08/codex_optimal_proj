
def reverse(n):
    return int(str(n)[::-1])
a, b = input().split()
a = int(a)
b = int(b)
if reverse(a) > reverse(b):
    print(reverse(a))
else:print(reverse(b))
