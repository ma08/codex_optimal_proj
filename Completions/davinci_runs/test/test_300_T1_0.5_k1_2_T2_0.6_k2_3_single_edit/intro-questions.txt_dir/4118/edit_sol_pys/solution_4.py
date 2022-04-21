

def main():
    a, b, c = map(int, input().split())
    if a == b == c or a == b or a == c or b == c:
        print('No')
    elif (a + b) == c or (a + c) == b or (c + b) == a:
        print('No')
    elif (a + b + c) % 2 == 0:
        print('Yes')
    elif (a + b + c) % 2 == 1:
        print('No')

if __name__ == '__main__':
    main()
