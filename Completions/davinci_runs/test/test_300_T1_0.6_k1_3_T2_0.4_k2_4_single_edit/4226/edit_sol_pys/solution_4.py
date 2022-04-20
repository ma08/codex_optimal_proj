
x, y = map(int, input().split())
print("Yes" if y % 2 == 0 and 4 * x <= y and y <= 2 * x else "No")
