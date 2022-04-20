

def main():
    n, m = map(int, input().split())
    count = 0
    while n <= m:
        if n * 2 <= m:
            n *= 2
        elif n * 3 <= m:
            n *= 3
        else:
            print(-1)
            return
        count += 1
    print(count)

if __name__ == '__main__':
    main()
