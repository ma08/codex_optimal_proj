

def main():
    n = input()
    digits = [int(i) for i in list(n)]
    if int(n) % sum(digits) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
