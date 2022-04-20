

def main():
    n = int(input())
    a, b = map(int, input().split())

    print((n - a) % b)

if __name__ == '__main__':
    main()
