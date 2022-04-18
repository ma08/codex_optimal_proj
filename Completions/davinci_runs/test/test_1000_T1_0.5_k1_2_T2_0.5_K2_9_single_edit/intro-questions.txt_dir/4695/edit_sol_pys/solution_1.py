

def main():
    a, b, c, d = map(int, input().split())
    if a + b == c + d:
        print('Balanced')
    elif a + b < c + d:
        print('Right')
    elif a + b > c + d:
        print('Left')

if __name__ == '__main__':
    main()
