

def main():
    n = int(input())
    digits = [int(i) for i in str(n)]  # list comprehention
    if n % sum(digits) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
