

def main():
    n = int(input())
    b = [int(i) for i in input().split()]
    if n == 1:
        print(0)
        return
    if n == 2:
        print(0)
        return
    if n == 3:
        if b[1] - b[0] == b[2] - b[1] or b[1] - b[0] == 0 or b[2] - b[1] == 0:
            print(0)
            return
        else:
            print(-1)
            return
    if n > 3:
        diff = 0
        for i in range(1, n-1):
            if b[i] - b[i-1] != diff:
                if diff == 0:
                    diff = b[i] - b[i-1]
                else:
                    if b[i] - b[i-1] == 0:
                        continue
                    else:
                        print(-1)
                        return
        if b[n-1] - b[n-2] == diff or b[n-1] - b[n-2] == 0:
            print(n - 2)
        else:
            print(-1)
        return

if __name__ == '__main__':
    main()
