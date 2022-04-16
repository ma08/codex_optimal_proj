

def compute_area(a, b, c):
    return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)

def is_inside(a, b, c, d):
    area = compute_area(a, b, c)
    area_a = compute_area(a, b, d)
    area_b = compute_area(a, c, d)
    area_c = compute_area(b, c, d)
    if area == area_a + area_b + area_c:
        return True
    return False

def main():
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    n = int(input())
    trees = []
    for i in range(n):
        trees.append([int(x) for x in input().split()])
    count = 0
    for tree in trees:
        if is_inside(a, b, c, tree):
            count += 1
    area = compute_area(a, b, c)
    print("{:.1f}".format(area))
    print(count)

if __name__ == '__main__':
    main()
