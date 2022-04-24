

def main():
    a, b, c = map(int, input().split())
    print(min(c, b // a))

if __name__ == '__main__':
    main()
