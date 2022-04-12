

def compute_area_triangle(a, b, c):
    return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2.0)

def is_inside(a, b, c, tree):
    area = compute_area_triangle(a, b, c)
    area_a = compute_area_triangle(a, b, tree)
    area_b = compute_area_triangle(a, c, tree)
    area_c = compute_area_triangle(b, c, tree)
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
    area = compute_area_triangle(a, b, c)
    print("{:.1f}".format(area), end=" ")
    print(count)

if __name__ == '__main__':
    main()
