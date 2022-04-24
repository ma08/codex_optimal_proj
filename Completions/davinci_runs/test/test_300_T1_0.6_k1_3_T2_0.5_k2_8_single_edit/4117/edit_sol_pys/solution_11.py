

def main():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(n-2):  # i番目の辺
        for j in range(i+1, n-1):  # j番目の辺
            for k in range(j+1, n):  # k番目の辺
                if l[i] < l[j] + l[k] and l[j] < l[i] + l[k] and l[k] < l[i] + l[j]:  # 三角形の成立条件
                    ans += 1  # 三角形を数える
    print(ans)

if __name__ == '__main__':
    main()
