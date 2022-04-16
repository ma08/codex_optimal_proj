

import sys

def main():
    """
    n: the number of S-shaped pieces
    m: the number of c-shaped pieces
    """
    n, m = map(int, input().split())
    # n: the number of S-shaped pieces
    # m: the number of c-shaped pieces

    # c = (m - 2 * n) / 2
    # s = n - c
    # print(int(s + c))
    # if m < 2 * n:
    #     print(0)
    # else:
    #     if (m - 2 * n) % 2 == 0:
    #         print((m - 2 * n) // 2 + n)
    #     else:
    #         print((m - 2 * n) // 2 + n - 1)

    # if m < 2 * n:
    #     print(0)
    # else:
    #     print(min(m - 2 * n + n, n))
    print(min(m // 2, n))

if __name__ == '__main__':
    main()
