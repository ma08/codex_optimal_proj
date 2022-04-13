

from sys import stdin, stdout
import math

def is_on_line(a, b, c):
    return math.fabs((b[1] - a[1]) * (c[0] - b[0]) - (c[1] - b[1]) * (b[0] - a[0])) < 1e-5

def is_in_triangle(a, b, c, p):
    return is_on_line(a, b, p) or is_on_line(b, c, p) or is_on_line(c, a, p)

def main():
    a = list(map(float, stdin.readline().split()))
    b = list(map(float, stdin.readline().split()))
    c = list(map(float, stdin.readline().split()))
    n = int(stdin.readline())
    count = 0
    for i in range(n):
        p = list(map(float, stdin.readline().split()))
        if is_in_triangle(a, b, c, p):
            count += 1
    s = math.fabs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)
    stdout.write(str(s) + '\n' + str(count) + '\n')

if __name__ == '__main__':
    main()
