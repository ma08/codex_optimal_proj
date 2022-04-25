
# -----Answer 1-----
x, y = map(int, input().split())  # x = 左の足の本数, y = 右の足の本数

if y % 2 == 0:
    if (x * 2 + 4) / 2 == y:
        print("Yes")
    else:
        print("No")
else:
    print("No")

# -----Answer 2-----
x, y = map(int, input().split())  # x = 左の足の本数, y = 右の足の本数

if x * 2 <= y <= x * 4:
    if y % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
