

def main():
    n, k = map(int, input().split()) # n, kを取得
    a = list(map(int, input().split())) # aを取得
    count = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            num = int(str(a[i]) + str(a[j])) # 数字を結合してint型に変換
            if num % k == 0:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
