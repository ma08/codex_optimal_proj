

def main():
    n, m = [int(x) for x in input().split()]
    if n == m:
        print(0)
    elif n > m:
        print(-1)
    else:
        count = 0
        while n < m:
            if n * 2 < m and n * 3 < m:
                if n * 2 < n * 3:
                    n *= 2
                else:
                    n *= 3
            elif n * 2 < m:
                n *= 2
            elif n * 3 < m:
                n *= 3
            else:
                print(-1)
                return
            count += 1
        print(count)

if __name__ == "__main__":
    main()