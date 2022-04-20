
def main():
    n = int(input())
    b = [int(i) for i in input().split()]
    if n == 1 or n == 2 or n == 3:
        if b[1] - b[0] == b[2] - b[1] or n == 2 or n == 3:
            print(0)
            return 0
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
                    return -1
    print(n - 2)
    return n - 2

if __name__ == '__main__':
    main()
