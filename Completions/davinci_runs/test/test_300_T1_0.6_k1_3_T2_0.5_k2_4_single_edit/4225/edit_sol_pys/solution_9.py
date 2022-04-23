

def main():
    a, b, c, k = map(int, input().split())  # 入力を受け取る
    if k <= a:
        print(k)  # そのまま出力
    elif a < k <= a + b:
        print(a)  # aにする
    else:
        print(a - (k - a - b))  # 引く

if __name__ == '__main__':
    main()
