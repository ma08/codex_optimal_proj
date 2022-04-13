a, b = map(int, input().split())
print(max(a + b, a - b, a * b))

# if a + b > a - b and a + b > a * b:
#     print(a + b)
# elif a - b > a + b and a - b > a * b:
#     print(a - b)
# else:
#     print(a * b)
