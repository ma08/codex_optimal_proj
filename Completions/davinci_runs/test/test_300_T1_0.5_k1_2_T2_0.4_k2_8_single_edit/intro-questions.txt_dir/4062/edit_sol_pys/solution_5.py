

def main():
    a, b, c, d = map(int, input().split())  # 入力
    print(max(a * c, a * d, b * c, b * d))  # 出力

if __name__ == '__main__':
    main()
