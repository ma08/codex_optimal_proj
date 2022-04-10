

def main():
    n = int(input())
    s = input()
    print('NO') if n == 1 or (n == 2 and s[0] > s[1]) else print('YES\n' + '0' * n)

if __name__ == '__main__':
    main()