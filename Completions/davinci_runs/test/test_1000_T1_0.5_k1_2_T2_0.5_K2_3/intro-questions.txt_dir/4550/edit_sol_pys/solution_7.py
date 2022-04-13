

a, b, c = map(float, input().split())

if a == b and b == c:
    print("No")
elif a == b or b == c or a == c:
    print("Yes")
else:

    print("Yes")
