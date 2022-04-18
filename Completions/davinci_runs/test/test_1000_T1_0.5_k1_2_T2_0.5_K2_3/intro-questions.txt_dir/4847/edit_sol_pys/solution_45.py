

def compute_area(a, b, c):
    return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)

def isInside(a, b, c, point):
    area = compute_area(a, b, c)
    areaA = compute_area(a, b, point)
    areaB = compute_area(a, c, point)
    areaC = compute_area(b, c, point)
    if area == areaA + areaB + areaC:
        return True
    return False

def main():
    a = [int(x) for x in raw_input().split()]
    b = [int(x) for x in raw_input().split()]
    c = [int(x) for x in raw_input().split()]
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in raw_input().split()])
    count = 0
    for point in points:
        if isInside(a, b, c, point):
            count += 1
    area = compute_area(a, b, c)
    print("{:.1f}".format(area))
    print(count)

if __name__ == '__main__':
    main()
