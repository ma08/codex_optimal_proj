

def main():
    a, b = map(int, input().split()) # a, bにそれぞれ入力を代入

    if a == b:
        print(4 * a) # 縦横が等しい場合、縦横を4倍した数を出力
    else:
        print(2 * (a + b))

if __name__ == "__main__":
    main()
