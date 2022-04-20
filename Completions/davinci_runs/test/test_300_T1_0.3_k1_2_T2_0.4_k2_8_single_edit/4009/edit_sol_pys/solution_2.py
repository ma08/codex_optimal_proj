

def main():
    n, x, y = map(int, input().split())  # n: 桁数 x: 1を含む桁数 y: 0を含む桁数
    num = input()  # 数字
    ans = 0
    for i in range(y):  # 0を含む桁について
        if num[n - x + i] == '0':  # 0が入っている場合
            ans += 1
    for i in range(y, x):  # 1を含む桁について
        if num[n - x + i] == '1':  # 1が入っている場合
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
