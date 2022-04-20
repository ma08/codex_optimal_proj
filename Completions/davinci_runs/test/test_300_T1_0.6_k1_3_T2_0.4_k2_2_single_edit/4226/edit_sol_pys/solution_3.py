

def main():
    x, y = map(int, input().split())
    if x == y//2 or x < y//2 or x > y//2:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()
