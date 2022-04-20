

def main():
    n, x, y = map(int, input().split())
    num = input()
    ans = 0
    for i in range(n - x, n - x + y):
        if num[i] == '0':
            ans += 1
    for i in range(n - x + y, n - x + x):
        if num[i] == '1':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
