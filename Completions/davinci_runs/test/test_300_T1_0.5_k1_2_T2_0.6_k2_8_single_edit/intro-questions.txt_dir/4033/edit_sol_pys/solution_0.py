

def main():
    a, b = map(int, input().split())  # a,bにはそれぞれ数字が入る

    if a == b:  # aとbが等しい場合
        print(4 * a)  # 4*aの値を出力
    else:
        print(2 * (a + b))

if __name__ == "__main__":
    main()
