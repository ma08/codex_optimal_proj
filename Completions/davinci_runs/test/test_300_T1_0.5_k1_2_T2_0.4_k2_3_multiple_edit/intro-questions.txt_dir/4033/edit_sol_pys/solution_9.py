

def main():
    a, b = map(int, input().split())  # a, bをint型に変換して代入

    if a == b:
        print(4 * a)  # a = bならば4 * aを出力
    else:
        print(2 * (a + b))  # a != bならば2 * (a + b)を出力

if __name__ == "__main__":
    main()
