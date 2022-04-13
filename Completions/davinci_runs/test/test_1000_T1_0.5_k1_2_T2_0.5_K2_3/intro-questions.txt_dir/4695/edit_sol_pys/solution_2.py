

def main():
    x, y = map(int, input().split())
    if x <= 5 and y <= 5:
        print('Yes')
    if x <= 7 and y <= 7:
        print('Yes')
    if x <= 10 and y <= 10:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
