

a, b, c = [int(x) for x in input().split()]
x, y, z = [int(x) for x in input().split()]

if a == x and b == y and c == z:
    print("Boxes are equal")
elif a <= x and b <= y and c <= z:
    print("The first box is smaller than the second one")
elif a >= x and b >= y and c >= z:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
