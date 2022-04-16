

def compute_area(x, y):
    return abs((x[0] * (y[1] - z[1]) + y[0] * (z[1] - x[1]) + z[0] * (x[1] - y[1])) / 2)

def is_inside(x, y, z, tree):
    area = compute_area(x, y, z)
    area_a = compute_area(x, y, tree)
    area_b = compute_area(x, z, tree)
    area_c = compute_area(y, z, tree)
    if area == area_a + area_b + area_c:
        return True
    return False

def main():
    x = [int(x) for x in input().split()]
    y = [int(x) for x in input().split()]
    z = [int(x) for x in input().split()]
    n = int(input())
    trees = []
    for i in range(n):
        trees.append([int(x) for x in input().split()])
    count = 0
    for tree in trees:
        if is_inside(x, y, z, tree):
            count += 1
    area = compute_area(x, y, z)
    print("{:.1f}".format(area))
    print(count)

if __name__ == '__main__':
    main()
