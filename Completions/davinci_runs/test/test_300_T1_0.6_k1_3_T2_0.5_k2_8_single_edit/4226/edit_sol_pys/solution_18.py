

def main():
    x, y = map(int, input().split())
    if x == y:
        print('Yes')
    elif x > y:
        print('No')
    elif x < y:
        print('No')

if __name__ == '__main__':
    main()
