

def main():
    n, m = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    b = sorted(a)
    if n % 2 == 1:
        med = b[n//2]
    else:
        med = (b[n//2 - 1] + b[n//2]) // 2
    if med != m:
        print(0)
    else:
        count = 0
        for i in range(n):
            if a[i] == med:
                count += 1
        print((count * (count - 1)) // 2)

if __name__ == '__main__':
    main()
