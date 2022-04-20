

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    if n == 1:
        print(0)
        return
    if n == 2:
        print(0)
        return
    if n == 3:
        if a[1] - a[0] == a[2] - a[1]:
            print(0)
            return
        else:
            print(-1)
            return
    if n > 3:
        diff = a[1] - a[0]
        for i in range(1, n):
            if a[i] - a[i-1] != diff:
                if diff == 0:
                    diff = a[i] - a[i-1]
                else:
                    if a[i] - a[i-1] == 0:
                        continue
                    else:
                        print(-1)
                        return
        print(n - 2)
        return

if __name__ == '__main__':
    main()
