

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()  # 等差数列を作るためにソート
    a.append(0)  # 前と同じ数字なら等差数列を作れる
    cnt = 0
    ans = 0
    for i in range(1, n+1):
        if a[i] == a[i-1]:  # 前と同じ数字なら等差数列を作れる
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1
    print(ans)


if __name__ == '__main__':
    main()
