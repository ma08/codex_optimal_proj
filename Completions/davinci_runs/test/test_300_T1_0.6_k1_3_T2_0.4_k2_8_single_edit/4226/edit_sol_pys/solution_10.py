

def main():
    x, y = map(int, input().split())
    if x == y//2 and x+y == 0:
        print('Yes')
    elif x > y//2 and x+y == 0:
        print('No')
    elif x < y//2 and x+y == 0:
        print('No')

if __name__ == '__main__':
    main()
