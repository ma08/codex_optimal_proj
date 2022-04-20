a, b, c = list(map(int, input().split()))
if a == b == c:
    print("No")
    exit()


if a == b or a == c or b == c:
    print("Yes")
