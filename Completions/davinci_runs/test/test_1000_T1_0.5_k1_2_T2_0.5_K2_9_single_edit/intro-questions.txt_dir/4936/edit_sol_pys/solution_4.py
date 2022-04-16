

import sys

def main():
    a = int(sys.stdin.readline().strip())
    b = int(sys.stdin.readline().strip())
    c = int(sys.stdin.readline().strip())
    d = int(sys.stdin.readline().strip())
    e = int(sys.stdin.readline().strip())
    f = int(sys.stdin.readline().strip())
    g = int(sys.stdin.readline().strip())
    h = int(sys.stdin.readline().strip())
    i = int(sys.stdin.readline().strip())
    if a + b + c == d + e + f == g + h + i == a + d + g == b + e + h == c + f + i == a + e + i == c + e + g:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
