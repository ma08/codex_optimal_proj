

a, b, c = map(int, input().split())  # input

if a == b and b != c:  # if
    print("Yes")
elif a == c and b != c:  # else if
    print("Yes")
elif b == c and a != c:  # else if
    print("Yes")
else:  # else
    print("No")
