

def main():
    n, x, y = map(int, input().split())
    num = input()
    ans = 0
    for i in range(x):
        if num[n - x + i] == '0' and i >= y:
            ans += 1
        if num[n - x + i] == '1' and i < y:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
