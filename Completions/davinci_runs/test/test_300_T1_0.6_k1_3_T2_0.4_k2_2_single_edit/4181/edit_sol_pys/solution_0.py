

def main(n, p, q):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    a = [0] * (n + 1)
    a[0] = 1
    a[1] = 1
    a[2] = 2
    a[3] = 4
    for i in range(4, n + 1):
        a[i] = a[i - 1] + a[i - 2] + a[i - 3] + a[i - 4]

    return a[n]

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(main(n, p, q))
