

def main():
    x, y = map(int, input().split())
    if x <= 4 <= y:
        print('Yes')
    elif x <= 8 <= y:
        print('Yes')
    elif x <= 12 <= y:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
