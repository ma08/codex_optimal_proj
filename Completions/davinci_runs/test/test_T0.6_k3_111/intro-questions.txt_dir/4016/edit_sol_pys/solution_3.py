

def main():
    n, k = map(int, input().split())  # n:文字列の長さ, k:繰り返し回数
    t = input()  # 文字列

    s = ''  # 繰り返した文字列
    for i in range(k):
        s += t

    print(s)


if __name__ == '__main__':
    main()
