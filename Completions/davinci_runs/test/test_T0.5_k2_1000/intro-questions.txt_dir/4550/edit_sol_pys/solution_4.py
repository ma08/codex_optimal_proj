
a, b, c = map(int, input().split())

if a == b and b == c:
    print("No")
elif a == b or b == c or a == c:
    print("No")
else:
    print("Yes")
