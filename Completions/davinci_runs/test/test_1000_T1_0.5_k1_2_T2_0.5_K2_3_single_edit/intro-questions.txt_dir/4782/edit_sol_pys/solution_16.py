

def main():
    n, m = map(int, input().split())
    print(max(m, n-m)*(n-max(m, n-m)) + min(m, n-m))

if __name__ == '__main__':
    main()
