

def main():
    a, b, c, d = map(int, input().split())
    print(min(a+b, a+d, b+d, c+d))

if __name__ == '__main__':
    main()
