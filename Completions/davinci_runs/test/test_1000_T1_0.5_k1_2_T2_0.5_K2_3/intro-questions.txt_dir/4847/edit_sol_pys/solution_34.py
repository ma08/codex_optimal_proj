
def area_triangle(a, b, c):  # вычисление площади треугольника по координатам вершин
    return abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2.0


def contains(a, b, c, p):  # проверка принадлежности точки площади треугольника
    return area_triangle(a, b, c) == area_triangle(a, b, p) + area_triangle(a, p, c) + area_triangle(p, b, c) + 1e-6


if __name__ == "__main__":
    a, b, c = tuple(map(int, input().split()))
    n = int(input())
    count = 0.0
    for i in range(n):
        p = tuple(map(int, input().split()))
        if contains(a, b, c, p):
            count += 1
    print("%.1f" % area_triangle(a, b, c))
    print(count)
