

def main():
    a, b = map(int, input().split())
    print(b - a - 1 if b - a > 1 else 0)

if __name__ == '__main__':
    main()
