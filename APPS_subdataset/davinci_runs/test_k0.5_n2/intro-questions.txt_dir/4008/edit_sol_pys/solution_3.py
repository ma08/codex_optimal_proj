
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_set = set(a)  # 重複を削除したリスト
    if len(a_set) > k:  # 重複を削除したリストの要素数がkより大きい場合は色が足りないのでNO
        print("NO")
        return
    color = [0 for _ in range(n)]  # 色を格納するリスト
    for i in range(n):
        color[i] = (a[i] - 1) % k + 1
    print("YES")
    print(*color)

if __name__ == "__main__":
    main()
