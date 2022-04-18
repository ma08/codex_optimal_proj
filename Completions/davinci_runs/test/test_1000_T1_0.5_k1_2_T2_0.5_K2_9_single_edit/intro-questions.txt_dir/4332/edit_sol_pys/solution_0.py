

def main():
    num = int(input())
    digits = [int(i) for i in str(num)]
    if num % sum(digits) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
