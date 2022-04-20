

def main():
    n, x, y = map(int, input().split())  # n: 桁数, x: 先頭から貼り替える桁数, y: 後ろから貼り替える桁数
    num = input()
    ans = 0
    for i in range(y):  # 後ろから貼り替える桁数のループ
        if num[n - x + i] == '0':  # 後ろから貼り替える桁数のループで0があれば+1
            ans += 1
    for i in range(y, x):  # 先頭から貼り替える桁数のループ
        if num[n - x + i] == '1':  # 先頭から貼り替える桁数のループで1があれば+1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
