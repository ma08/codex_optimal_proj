

# a, b, x = map(int, input().split())

# s = "0"*a + "1"*b

# for i in range(a):
#     for j in range(b):
#         if i + j == x:
#             print(s)
#             exit()
#         s = s[1:] + s[0]

a, b, c = map(int, input().split())

if a + b == c and a - b == c:
    print("?")
elif a + b == c:
    print("+")
elif a - b == c:
    print("-")
else:
    print("!")
