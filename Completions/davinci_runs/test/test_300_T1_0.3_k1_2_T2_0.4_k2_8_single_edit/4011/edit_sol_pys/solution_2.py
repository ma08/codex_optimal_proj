

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f_inv = [0] * 10
    for i in range(1, 10):
        f_inv[f[i - 1]] = i
    a_new = [f_inv[int(a[i])] for i in range(n)]
    a_new = [str(a_new[i]) for i in range(n)]
    a_new = ''.join(a_new)
    print(a_new)

if __name__ == '__main__':
    main()
