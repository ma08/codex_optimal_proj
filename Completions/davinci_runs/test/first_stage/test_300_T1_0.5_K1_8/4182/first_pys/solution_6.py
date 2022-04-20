

# My code
n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if (y - x) < (max(a) - min(b)):
    print("War")
else:
    print("No War")

# Other's code
# n, m, x, y = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# if max(a) < min(b):
#     print("No War")
# else:
#     print("War")