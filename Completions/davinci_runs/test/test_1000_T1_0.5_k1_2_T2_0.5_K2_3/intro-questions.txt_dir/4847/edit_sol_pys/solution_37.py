
def area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2


x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]
x3, y3 = [int(i) for i in input().split()]

n = int(input())
trees = []
for i in range(n):
    x, y = [int(i) for i in input().split()]
    trees.append((x, y))

A = area(x1, y1, x2, y2, x3, y3)
count = 0
for x, y in trees:
    if inside(x1, y1, x2, y2, x3, y3, x, y):
        count += 1

print("%.1f" % A)  # %.1f is a format specifier
print(count)
