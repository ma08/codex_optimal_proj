

# # Read input
# k, x = map(int, input().split())

# # Check if the coins add up to X yen or more.
# if k * 500 >= x:
#     print('Yes')
# else:
#     print('No')

a = int(input())
b = int(input())
c = int(input())

if a + b == c:
    print("{}+{}={}".format(a, b, c))
elif a - b == c:
    print("{}-{}={}".format(a, b, c))
elif a * b == c:
    print("{}*{}={}".format(a, b, c))
elif a / b == c:
    print("{}/{}={}".format(a, b, c))
elif a == b + c:
    print("{}={}+{}".format(a, b, c))
elif a == b - c:
    print("{}={}-{}".format(a, b, c))
elif a == b * c:
    print("{}={}*{}".format(a, b, c))
elif a == b / c:
    print("{}={}/{}".format(a, b, c))
else:
    print("None")
