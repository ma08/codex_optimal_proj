
def main():
    x, y = map(int, input().split())
    if x <= 4 and y <= 4:
        print('Yes')
    elif x <= 8 and y <= 4:
        print('Yes')
    elif x <= 12 and y <= 4:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
