

from sys import stdin, stdout
import math

def is_on_line(p1, p2, p3):
    return math.fabs((p2[1] - p1[1]) * (p3[0] - p2[0]) - (p3[1] - p2[1]) * (p2[0] - p1[0])) < 1e-5

def is_in_triangle(p1, p2, p3, p):
    return is_on_line(p1, p2, p) or is_on_line(p2, p3, p) or is_on_line(p3, p1, p)

def main():
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))
    n = int(stdin.readline())
    count = 0
    for i in range(n):
        p = list(map(int, stdin.readline().split()))
        if is_in_triangle(a, b, c, p):
            count += 1
    s = math.fabs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)
    stdout.write('{:.1f}\n{}\n'.format(s, count))

if __name__ == '__main__':
    main()
