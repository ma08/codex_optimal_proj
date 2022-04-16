
def main():
    x, y = map(int, input().split())
    print('Yes' if x <= 4 and y <= 4 else 'No')
    print('Yes' if x <= 8 and y <= 8 else 'No')
    print('Yes' if x <= 12 and y <= 12 else 'No')

if __name__ == '__main__':
    main()
