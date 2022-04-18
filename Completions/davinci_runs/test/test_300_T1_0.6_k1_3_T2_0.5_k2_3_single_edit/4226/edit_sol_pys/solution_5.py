

def main():
    a, b = map(int, input().split())
    if a == b//2:
        print('YES')
    elif a > b//2:
        print('NO')
    elif a < b//2:
        print('NO')

if __name__ == '__main__':
    main()
