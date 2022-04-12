

def main():
    N = int(input())
    if N % sum([int(i) for i in str(N)]) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
