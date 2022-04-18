

def main():
    n = int(input())  # 標準入力から整数を取得
    a = list(map(int, input().split()))  # 標準入力から整数の配列を取得

    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]

    print(alice - bob)  # 出力

if __name__ == "__main__":
    main()
