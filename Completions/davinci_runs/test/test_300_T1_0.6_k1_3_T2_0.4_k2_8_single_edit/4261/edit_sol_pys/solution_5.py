

def main():
    a, b, c = map(int, input().split())
    print(max(c - (a - b), 0))

if __name__ == '__main__':
    main()
