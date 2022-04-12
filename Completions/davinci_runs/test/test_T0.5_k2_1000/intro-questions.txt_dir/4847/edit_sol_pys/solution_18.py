

def compute_area(a, b, c):  # 计算三角形面积
    return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)

def is_inside(a, b, c, tree):  # 判断树是否在三角形内
    area = compute_area(a, b, c)
    area_a = compute_area(a, b, tree)
    area_b = compute_area(a, c, tree)
    area_c = compute_area(b, c, tree)
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
    print("{:.1f}".format(compute_area(a, b, c)))
    print(count)

if __name__ == '__main__':
    main()
