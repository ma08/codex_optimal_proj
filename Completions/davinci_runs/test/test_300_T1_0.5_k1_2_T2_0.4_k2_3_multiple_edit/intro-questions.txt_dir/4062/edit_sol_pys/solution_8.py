def main():
    a, b, c, d = map(int, input().split())  # 入力を受け取る
    print(max(a * c, a * d, b * c, b * d))  # 出力する

if __name__ == '__main__':
    main()
