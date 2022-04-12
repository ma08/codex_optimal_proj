

def get_expected(n, k, d):
    if k == 1:
        return n/d
    if n == 1:
        return 1
    return (n/d) + get_expected(n-1, k-1, d)

def main():
    n, k = map(int, input().split())
    print(get_expected(n, k, 2))

if __name__ == '__main__':
    main()
