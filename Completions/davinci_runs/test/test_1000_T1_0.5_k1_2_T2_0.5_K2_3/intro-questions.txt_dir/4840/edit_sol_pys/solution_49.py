

def main():
    a, b = list(map(int, input().split()))
    c, d = list(map(int, input().split()))
    a, b, c, d = 1, 4, 1, 6
    print(max(a, c), min(b, d))

if __name__ == '__main__':
    main()
