

def main():
    n, m = map(int, input().split())
    if n >= m:
        print(0)
    else:
        print(m - n)

if __name__ == '__main__':
    main()
