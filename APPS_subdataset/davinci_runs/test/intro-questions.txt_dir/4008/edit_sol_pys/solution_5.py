
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_set = set(a)  # 重複を削除
    if len(a_set) > k:  # 重複を削除した数がkより多い場合は色を塗ることはできない
        print("NO")
        return
    color = [0 for _ in range(n)]
    for i in range(n):
        color[i] = (a[i] - 1) % k + 1  # 同じ数字は同じ色を塗る
    print("YES")
    print(*color)

if __name__ == "__main__":
    main()
