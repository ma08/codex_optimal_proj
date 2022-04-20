

a, b, c = map(int, input().split()) #take 3 inputs and split them

if a == b and b != c: #if a is equal to b and b is not equal to c
    print("Yes")
elif a == c and b != c:
    print("Yes")
elif b == c and a != c:
    print("Yes")
else:
    print("No")
