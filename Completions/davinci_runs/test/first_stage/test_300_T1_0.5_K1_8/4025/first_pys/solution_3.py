

def main():
    a, b, c = map(int, input().strip().split())
    print(min(a, b, c) * 7 + 3)

if __name__ == '__main__':
    main()