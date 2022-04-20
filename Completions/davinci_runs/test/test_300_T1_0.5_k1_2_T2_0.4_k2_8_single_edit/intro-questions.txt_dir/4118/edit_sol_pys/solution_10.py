

def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    if n > 20 or n < 1 or m > 20 or m < 1:
        print(-1)
        return
    print(n * m)

if __name__ == '__main__':
    main()
