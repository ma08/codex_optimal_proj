
# -----Answer 1-----
x, y = map(int, input().split())  # input

if y % 2 == 0 and (x * 2 + 4) / 2 == y:
    print("Yes")
else: print("No")

# -----Answer 2-----
x, y = map(int, input().split())  # input

if x * 2 <= y <= x * 4 and y % 2 == 0:
    print("Yes")
else:
    print("No")
