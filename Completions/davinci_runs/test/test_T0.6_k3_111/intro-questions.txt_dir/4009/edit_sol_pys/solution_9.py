

def main():
    n, x, y = map(int, input().split())
    num = input().strip()
    remainder = int(num[:x]) % (10**y)
    if remainder == 0:
        print(0)
        return
    
    ans = 0
    for i in range(x - y):
        if num[i] == '1':
            ans += 1
    for i in range(x - y, x):
        if num[i] == '0':
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
