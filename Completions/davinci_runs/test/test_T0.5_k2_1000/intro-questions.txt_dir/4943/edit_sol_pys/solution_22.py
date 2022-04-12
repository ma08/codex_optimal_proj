

from math import sqrt
from sys import stdin

def read_input():
    N = int(stdin.readline().strip())
    points = []
    for i in range(N):
        x, y = [float(x) for x in stdin.readline().strip().split()]  # читаем координаты вершин
        points.append((x, y))
    A = float(stdin.readline().strip())  # читаем площадь
    return N, points, A

def print_output(points):
    for x, y in points:  # выводим координаты вершин
        print(x, y)

def get_area(points):
    area = 0.0  # вычисляем площадь
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % len(points)]
        area += x1*y2 - x2*y1
    return abs(area / 2.0)

def get_centroid(points):
    x_sum = 0.0  # вычисляем центр масс
    y_sum = 0.0
    for x, y in points:
        x_sum += x
        y_sum += y
    return x_sum / len(points), y_sum / len(points)

def get_rescaled_points(points, A):
    old_area = get_area(points)  # вычисляем коэффициент масштабирования
    ratio = sqrt(A / old_area)  # и применяем его к вершинам
    cx, cy = get_centroid(points)
    rescaled_points = []
    for x, y in points:
        rescaled_points.append(((x-cx)*ratio, (y-cy)*ratio))
    return rescaled_points

def main():
    N, points, A = read_input()  # читаем входные данные
    rescaled_points = get_rescaled_points(points, A)  # вычисляем новые координаты вершин
    print_output(rescaled_points)  # выводим результат

if __name__ == '__main__':
    main()
