

a, b, c = map(str, input().split())

if a[-1] == b[0]:
    print("Yes")
elif b[-1] == c[0]:
    print("Yes")
elif a[-1] == c[0]:
    print("Yes")
else:
    print("No")
