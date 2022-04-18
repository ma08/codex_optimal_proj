


import sys

def main():
    s, v1, v2 = [int(x) for x in sys.stdin.readline().split()]

    if s < v1 and s < v2:
        print('Impossible')
        return

    n1 = s // v1
    n2 = (s - (n1 * v1)) // v2
    while n1 >= 0 and n2 * v2 < (s - (n1 * v1)):
        n2 += 1
        if n2 * v2 > (s - (n1 * v1)):
            n1 -= 1
            n2 = (s - (n1 * v1)) // v2

    if n1 * v1 + n2 * v2 != s:
        print('Impossible')
        return

    print(n1, n2)


if __name__ == '__main__':
    main()
