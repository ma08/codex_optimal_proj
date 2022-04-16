

def main():
    n = int(input())
    print('Yes' if n % sum([int(i) for i in str(n)]) == 0 else 'No')


if __name__ == '__main__':
    main()
