

def main():
    n = int(input())
    num_list = [int(i) for i in str(n)]
    if n % sum(num_list) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
