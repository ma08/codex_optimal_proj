
from math import sqrt

def main():
    # read input
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    A = int(input())

    # find center of mass
    x_c = 0.0
    y_c = 0.0
    for i in range(N):
        x_c += points[i][0]
        y_c += points[i][1]
    x_c /= N
    y_c /= N

    # find area of original polygon
    A_0 = 0
    for i in range(N):
        A_0 += (points[i][0] - x_c) * (points[i][1] - y_c)
    A_0 = abs(A_0)

    # find scale factor
    s = A / A_0

    # find new points
    new_points = []
    for i in range(N):
        x = (points[i][0] - x_c) * s + x_c
        y = (points[i][1] - y_c) * s + y_c
        new_points.append((x, y))

    # find translation
    x_min = float("infinity")
    y_min = float("infinity")
    for i in range(N):
        if new_points[i][0] < x_min:
            x_min = new_points[i][0]
        if new_points[i][1] < y_min:
            y_min = new_points[i][1]
    for i in range(N):
        new_points[i] = (new_points[i][0] - x_min, new_points[i][1] - y_min)

    # print new points
    for i in range(N):
        print(round(new_points[i][0], 2), round(new_points[i][1], 2))

if __name__ == "__main__":
    main()
