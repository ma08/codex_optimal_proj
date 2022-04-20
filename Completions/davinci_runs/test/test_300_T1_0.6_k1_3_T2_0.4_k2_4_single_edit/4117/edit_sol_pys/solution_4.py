

def main():
    n = int(input())
    l = list(map(int, input().split()))  # 入力をリストに
    ans = 0
    for i in range(n-2):  # iを0からn-3まで
        for j in range(i+1, n-1):  # jをi+1からn-2まで
            for k in range(j+1, n):  # kをj+1からn-1まで
                if l[i] + l[j] > l[k] and l[i] + l[k] > l[j] and l[j] + l[k] > l[i]:
                    # 三角形の条件を満たしていれば、ansをインクリメント
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
