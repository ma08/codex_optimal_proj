

def main():
    k, x = map(int, input().split())
    if k * 500 >= x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
