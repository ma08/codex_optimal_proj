
def compute_area(a, b, c):
    return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)

def is_inside(a, b, c, tree):
    area = compute_area(a, b, c)
    area_a = abs(compute_area(a, b, tree))
    area_b = abs(compute_area(a, c, tree))
    area_c = abs(compute_area(b, c, tree))
    return area == area_a + area_b + area_c

def main():
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    n = int(input())
    trees = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for tree in trees:
        if is_inside(a, b, c, tree):
            count += 1
    area = compute_area(a, b, c)
    print("{:.1f}".format(area))
    print(count)

if __name__ == '__main__':
    main()
