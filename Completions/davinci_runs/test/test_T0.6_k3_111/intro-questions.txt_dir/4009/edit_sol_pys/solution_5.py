

def main():
    n, x, y = map(int, input().split())
    num = input()
    ans = 0
    if x >= y:
        mod_number = int(num[:x])
        remainder = mod_number % (10**y)
        if remainder == 0:
            return 0
        
        for i in range(x - y):
            if num[i] == '1':
                ans += 1
        for i in range(x - y, x):
            if num[i] == '0':
                ans += 1
    else:
        mod_number = int(num[:y])
        remainder = mod_number % (10**x)
        if remainder == 0:
            return 0
        
        for i in range(y - x):
            if num[i] == '1':
                ans += 1
        for i in range(y - x, y):
            if num[i] == '0':
                ans += 1
    return ans


if __name__ == '__main__':
    print(main())
