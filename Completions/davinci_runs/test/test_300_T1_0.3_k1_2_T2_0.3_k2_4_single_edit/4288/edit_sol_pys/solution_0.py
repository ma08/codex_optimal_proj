

a, b, c = map(int, input().split()) # input 3 numbers

if a == b and b != c: # if 2 numbers are equal and the other is not
    print("Yes")
elif a == c and b != c:
    print("Yes")
elif b == c and a != c:
    print("Yes")
else:
    print("No")
