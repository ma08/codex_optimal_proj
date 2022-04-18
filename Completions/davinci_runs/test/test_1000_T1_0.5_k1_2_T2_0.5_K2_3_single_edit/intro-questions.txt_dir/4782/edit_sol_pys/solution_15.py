

def main():
    n, m = map(int, input().split())
    print(max(m, n-m)*(n-max(m, n-m)+1) + m)

if __name__ == '__main__':
    main()
