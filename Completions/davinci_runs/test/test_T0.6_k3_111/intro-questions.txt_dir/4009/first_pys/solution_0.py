

def main():
    n, x, y = map(int, input().split())
    num = input().strip()
    mod_num = int(num[:x])
    remainder = mod_num % (10**y)
    if remainder == 0:
        return 0
    
    ans = 0
    for i in range(x - y):
        if num[i] == '1':
            ans += 1
    for i in range(x - y, x):
        if num[i] == '0':
            ans += 1
    return ans


if __name__ == '__main__':
    print(main())