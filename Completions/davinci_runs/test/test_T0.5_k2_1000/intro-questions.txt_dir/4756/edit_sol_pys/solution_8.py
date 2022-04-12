

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    if n % 2 == 1:
        a_n = a[n // 2]
        b_n = b[n // 2]
    else:
        a_n = (a[n // 2 - 1] + a[n // 2]) // 2
        b_n = (b[n // 2 - 1] + b[n // 2]) // 2
    print(b_n - a_n)

if __name__ == '__main__':
    main()
