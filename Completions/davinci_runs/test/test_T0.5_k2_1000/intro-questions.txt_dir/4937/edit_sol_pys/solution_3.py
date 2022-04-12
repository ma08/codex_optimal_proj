

def main():
    n, a = map(int, input().split())  # n: 個数, a: 容量
    e = list(map(int, input().split()))  # e: 容量のリスト
    e.sort()  # 容量の昇順にソート
    i = 0
    while a > 0 and i < n:
        if a >= e[i]:  # 入れられるなら入れる(入れられないならそのまま)
            a -= e[i]
            i += 1
        else:
            break
    print(i)

if __name__ == "__main__":
    main()
