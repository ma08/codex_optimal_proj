
a, b, x = map(int, input().split())

if a == b:
    print("0" * a + "1" * b, end="")
elif a > b:
    s = "0" * a + "1" * b
    for i in range(x):
        s = s[:i] + "1" + s[i+1:]
    print(s, end="")
else:
    s = "0" * a + "1" * b
    for i in range(x):
        s = s[:i] + "0" + s[i+1:]
    print(s, end="")
