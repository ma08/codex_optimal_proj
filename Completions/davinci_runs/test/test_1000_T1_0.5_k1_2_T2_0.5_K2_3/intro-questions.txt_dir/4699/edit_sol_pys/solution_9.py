

def main():
    n, k = map(int, input().split())
    d = set(map(int, input().split()))

    for i in range(n, n + 10 ** 5):
        if not any(s in d for s in str(i)):  # any()は条件に当てはまるものがあるかどうかを判定する
            print(i)
            exit()


if __name__ == '__main__':
    main()
