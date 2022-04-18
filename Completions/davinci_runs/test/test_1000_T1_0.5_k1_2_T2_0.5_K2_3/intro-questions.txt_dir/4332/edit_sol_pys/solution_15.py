

def main():
    n = int(input())
    number_list = [int(i) for i in str(n)]
    if n % sum(number_list) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
