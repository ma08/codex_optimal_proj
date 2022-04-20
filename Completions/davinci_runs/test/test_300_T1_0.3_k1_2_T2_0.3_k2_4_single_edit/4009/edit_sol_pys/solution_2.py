

def main():
    n, x, y = map(int, input().split())
    num = input()
    ans = 0
    for i in range(1, y + 1):
        if num[n - x + i] == '0':
            ans += 1
    for i in range(y + 1, x + 1):
        if num[n - x + i] == '1':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
