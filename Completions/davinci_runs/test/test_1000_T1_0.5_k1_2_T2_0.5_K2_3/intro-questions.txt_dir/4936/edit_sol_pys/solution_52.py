

def main():
    n = int(input())
    s = input()
    if n % 2 == 1:
        print('No')
    else:
        left = s[:n // 2]
        right = s[n // 2:]
        if left == right:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
