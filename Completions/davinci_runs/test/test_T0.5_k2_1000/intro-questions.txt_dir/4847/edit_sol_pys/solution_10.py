

from sys import stdin, stdout
import math

def is_on_line(p1, p2, p3, eps=1e-5):
    return math.fabs((p2[1] - p1[1]) * (p3[0] - p2[0]) - (p3[1] - p2[1]) * (p2[0] - p1[0])) < eps

def is_in_triangle(p1, p2, p3, p4, eps=1e-5):
    return is_on_line(p1, p2, p4, eps) or is_on_line(p2, p3, p4, eps) or is_on_line(p3, p1, p4, eps)

def main():
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))
    n = int(stdin.readline())
    count = 0
    for i in range(n):
        p = list(map(int, stdin.readline().split()))
        if is_in_triangle(a, b, c, p, eps=1e-1):
            count += 1
    s = math.fabs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)
    stdout.write('{:.1f}\n{}\n'.format(s, count))

if __name__ == '__main__':
    main()
