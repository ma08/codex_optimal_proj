

def main():
    n, x, y = map(int, input().split())
    num = input()
    ans = 0
    for i in range(x):
        if i < y and num[n - x + i] == '0':
            ans += 1 
        elif i >= y and num[n - x + i] == '1':
            ans += 1 
    print(ans)

if __name__ == '__main__':
    main()
