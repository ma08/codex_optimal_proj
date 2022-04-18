
def main():
    a, b, c = map(int, input().split())  # 入力を整数に変換
    if a == b or b == c or a == c:  # a == b or b == c or a == c のいずれかが真なら
        print("Yes")  # Yesを出力
    else:  # そうでないなら
        print("No")  # Noを出力

if __name__ == '__main__':
    main()
