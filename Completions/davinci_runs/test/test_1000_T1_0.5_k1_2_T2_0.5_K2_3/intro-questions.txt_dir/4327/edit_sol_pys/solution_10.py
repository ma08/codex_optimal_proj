# coding: utf-8


def main():
    a, p = map(int, input().split())
    print(p // 2 + (a + p % 2) * 3 // 2)


if __name__ == '__main__':
    main()
