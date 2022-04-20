

def main():
    n = int(input())
    b = [int(i) for i in input().split()]
    if n == 1:
        print(0)
        return
    diff = b[1] - b[0]
    for i in range(1, n):
        if b[i] - b[i-1] != diff:
            if diff == 0:
                diff = b[i] - b[i-1]
            else:
                if b[i] - b[i-1] == 0:
                    continue
                else:
                    print(-1)
                    return
    print(n - 2)
    return

if __name__ == '__main__':
    main()
