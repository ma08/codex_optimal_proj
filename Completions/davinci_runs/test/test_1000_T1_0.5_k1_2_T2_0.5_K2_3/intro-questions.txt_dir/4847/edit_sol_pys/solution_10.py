
def compute_area(a, b, c):
    return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)

def is_inside(a, b, c, point):
    area = compute_area(a, b, c)
    area_a = compute_area(a, b, point)
    area_b = compute_area(a, c, point)
    area_c = compute_area(b, c, point)
    if area == area_a + area_b + area_c:
        return True
    return False

def main():
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    count = 0
    for point in points:
        if is_inside(a, b, c, point):
            count += 1
    area = compute_area(a, b, c)
    print("{:.1f}".format(area))
    print(count)

if __name__ == '__main__':
    main()
