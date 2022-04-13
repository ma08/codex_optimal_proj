a, b, c = map(int, input().split())  # a, b, c = int(input().split())

if a == b and b == c:
    print("Yes")
elif a == c or b == c:
    print("Yes")
else:
    print("No")
