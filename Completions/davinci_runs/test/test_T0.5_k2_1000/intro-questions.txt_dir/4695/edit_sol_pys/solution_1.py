

def main():
    x, y = map(int, input().split())
    if x <= 12 and y <= 12 and x >= 1 and y >= 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
