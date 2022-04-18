

def main():
    n = input()
    if int(n) % sum([int(i) for i in list(n)]) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
