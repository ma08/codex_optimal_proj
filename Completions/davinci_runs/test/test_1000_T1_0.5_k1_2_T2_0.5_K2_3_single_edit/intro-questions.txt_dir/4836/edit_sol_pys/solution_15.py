

def main():
    n, c = map(int, input().split()) # n: 個数 c: 容量
    w = list(map(int, input().split())) # 重さ
    fruits = sorted(w) # 重さでソート

    i = 0
    total = 0
    while i < n:
        if total + fruits[i] <= c:
            total += fruits[i]
            i += 1
        else:
            break

    print(i)

if __name__ == "__main__":
    main()
