

def main():
    n, m = [int(x) for x in input().split()]
    if m % n != 0:
        print(-1)
        return
    if n == m:
        print(0)
        return
    cnt = 0
    while m != n:
        if m % 2 == 0:
            m //= 2
            cnt += 1
        elif m % 3 == 0:
            m //= 3
            cnt += 1
        else:
            print(-1)
            return
    print(cnt)

if __name__ == '__main__':
    main()