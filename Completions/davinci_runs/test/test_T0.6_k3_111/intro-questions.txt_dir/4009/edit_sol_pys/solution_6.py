

def main():
    n, x, y = map(int, input().split())
    num = input().strip()
    mod_num = int(num[:x]) % (10 ** y)
    remainder = mod_num % (10 ** (y - 1))
    if remainder != 0:
        return -1

    ans = 0
    for i in range(x - y):
        if num[i] == '1':
            ans += 1
    for i in range(x - y, x):
        if num[i] == '0':
            ans += 1
    return ans + 1


if __name__ == '__main__':
    print(main())
