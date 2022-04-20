

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f_inv = [0] * 10  # f_inv[i] = f^(-1)(i)
    for i in range(1, 10):
        f_inv[f[i - 1]] = i
    a = [f_inv[int(a[i])] for i in range(n)]  # a[i] = f^(-1)(a[i])
    a = [str(a[i]) for i in range(n)]  # a[i] = str(a[i])
    a = ''.join(a)  # a = a[0] + ... + a[n-1]
    print(a)  # print(a)

if __name__ == '__main__':
    main()
