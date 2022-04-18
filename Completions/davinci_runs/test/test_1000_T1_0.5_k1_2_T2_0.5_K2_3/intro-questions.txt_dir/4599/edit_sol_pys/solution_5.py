
def main():
    n = int(input()) # 整数の入力
    a = list(map(int, input().split())) # スペース区切りの整数の入力

    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]

    print(alice - bob)

if __name__ == "__main__":
    main()
