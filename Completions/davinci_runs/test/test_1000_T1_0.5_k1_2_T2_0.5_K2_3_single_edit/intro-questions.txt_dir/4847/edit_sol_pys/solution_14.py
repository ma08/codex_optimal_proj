

def area(x1, y1, x2, y2, x3, y3, x4, y4):
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2 + abs(x1*(y2-y4) + x2*(y4-y1) + x4*(y1-y2))/2

def inside(x1, y1, x2, y2, x3, y3, x4, y4, x, y):
    A = area(x1, y1, x2, y2, x3, y3, x4, y4)
    A1 = area(x, y, x2, y2, x3, y3, x4, y4)
    A2 = area(x1, y1, x, y, x3, y3, x4, y4)
    A3 = area(x1, y1, x2, y2, x, y, x4, y4)
    A4 = area(x1, y1, x2, y2, x3, y3, x, y)
    return A == A1 + A2 + A3 + A4

x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]
x4, y4 = [int(i) for i in input().split()]
x3, y3 = [int(i) for i in input().split()]

n = int(input())
trees = []
for i in range(n):
    x, y = [int(i) for i in input().split()]
    trees.append((x, y))

A = area(x1, y1, x2, y2, x3, y3, x4, y4)
count = 0
for x, y in trees:
    if inside(x1, y1, x2, y2, x3, y3, x4, y4, x, y):
        count += 1

print("%.1f" % A)
print(count)
