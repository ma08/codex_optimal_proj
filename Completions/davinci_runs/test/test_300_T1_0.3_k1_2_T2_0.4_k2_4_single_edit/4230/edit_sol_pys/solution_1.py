

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    print(min(range(101), key=lambda i: abs(i-x) if i not in p else 101))

if __name__ == '__main__':
    main()
