
def main():
    n = int(input())
    digits = [int(i) for i in str(n) if i != '0']
    if n % sum(digits) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
