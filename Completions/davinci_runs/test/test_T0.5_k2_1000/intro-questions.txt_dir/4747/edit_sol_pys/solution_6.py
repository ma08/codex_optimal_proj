

def get_expected(n, k):
    if k == 0:
        return n
    if n == 0:
        return 0
    return (n/2) + get_expected(n, k-1)

def main():
    n, k = map(int, input().split())
    print(get_expected(n, k))

if __name__ == '__main__':
    main()
