

def main():
    n, a = map(int, input().split())  # n: 個数, a: 金額
    count = 0
    e = list(map(int, input().split()))  # e: 値段
    e.sort()  # 値段を昇順にソート
    for i in range(n):
        if a >= e[i]:
            a -= e[i]
            count += 1
        else:
            break
    print(count)


if __name__ == '__main__':
    main()
